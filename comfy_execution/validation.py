from __future__ import annotations


def validate_node_input(
    received_type: str, input_type: str, strict: bool = False
) -> bool:
    """
    received_type and input_type are both strings of the form "T1,T2,...".

    If strict is True, the input_type must contain the received_type.
      For example, if received_type is "STRING" and input_type is "STRING,INT",
      this will return True. But if received_type is "STRING,INT" and input_type is
      "INT", this will return False.

    If strict is False, the input_type must have overlap with the received_type.
      For example, if received_type is "STRING,BOOLEAN" and input_type is "STRING,INT",
      this will return True.
    """
    # If either type is *, we allow any type
    if any(t == "*" for t in [received_type, input_type]):
        return True

    # If the types are exactly the same, we can return immediately
    if received_type == input_type:
        return True

    # Split the type strings into sets for comparison
    received_types = set(t.strip() for t in received_type.split(","))
    input_types = set(t.strip() for t in input_type.split(","))

    if strict:
        # In strict mode, all received types must be in the input types
        return received_types.issubset(input_types)
    else:
        # In non-strict mode, there must be at least one type in common
        return len(received_types.intersection(input_types)) > 0