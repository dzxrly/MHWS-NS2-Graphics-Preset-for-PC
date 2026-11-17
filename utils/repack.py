from __future__ import annotations

from typing import Any, Iterable

JsonDict = dict[str, Any]


def instances(data: JsonDict) -> JsonDict:
    value = data.get("_instances")
    if not isinstance(value, dict):
        raise ValueError("pack JSON is missing _instances")
    return value


def ref_id(ref: Any) -> int:
    if isinstance(ref, dict) and isinstance(ref.get("ref_instance_id"), int):
        return int(ref["ref_instance_id"])
    if isinstance(ref, int):
        return ref
    raise ValueError(f"expected ref_instance_id object, got {ref!r}")


def instance(data: JsonDict, ref: Any) -> JsonDict:
    idx = ref_id(ref=ref)
    entry = instances(data=data).get(str(idx))
    if not isinstance(entry, dict):
        raise KeyError(f"instance {idx} not found")
    return entry


def fields(data: JsonDict, ref: Any) -> JsonDict:
    value = instance(data=data, ref=ref).get("fields")
    if not isinstance(value, dict):
        raise ValueError(f"instance {ref_id(ref=ref)} has no fields")
    return value


def root_instance(data: JsonDict, class_suffix: str) -> JsonDict:
    roots = data.get("_roots")
    if not isinstance(roots, list):
        raise ValueError("pack JSON is missing _roots")
    for root in roots:
        entry = instance(data=data, ref=root)
        class_name = entry.get("_class")
        if isinstance(class_name, str) and class_name.endswith(class_suffix):
            return entry
    raise KeyError(f"root class not found: {class_suffix}")


def iter_ref_fields(data: JsonDict, refs: Any) -> Iterable[JsonDict]:
    if not isinstance(refs, list):
        raise ValueError(f"expected a list of refs, got {type(refs).__name__}")
    for ref in refs:
        yield fields(data=data, ref=ref)


def insert_instances_before(data: JsonDict, before: int, added: list[JsonDict]) -> None:
    # GraphicsPreset has no external RSZ userdata indices. Keep all referenced
    # objects before their owners as in the original instance table.
    if data["_rsz"]["userdata"]:
        raise ValueError("cannot reindex a GraphicsPreset with RSZ userdata")
    table = instances(data=data)
    shift = len(added)
    for entry in table.values():
        _shift_reference_ids(value=entry.get("fields"), before=before, shift=shift)
    data["_roots"] = [
        index + shift if index >= before else index for index in data["_roots"]
    ]
    data["_instances"] = {
        **{
            str(int(index) + shift if int(index) >= before else index): entry
            for index, entry in table.items()
        },
        **{str(index): entry for index, entry in enumerate(added, start=before)},
    }


def _shift_reference_ids(value: object, before: int, shift: int) -> None:
    if isinstance(value, dict):
        if "ref_instance_id" in value and value["ref_instance_id"] >= before:
            value["ref_instance_id"] += shift
        for child in value.values():
            _shift_reference_ids(value=child, before=before, shift=shift)
    elif isinstance(value, list):
        for child in value:
            _shift_reference_ids(value=child, before=before, shift=shift)
