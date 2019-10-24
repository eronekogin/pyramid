import colander


class TestForm(colander.MappingSchema):
    choice1 = colander.SchemaNode(
        colander.String(),
        missing=None
    )

    choice2 = colander.SchemaNode(
        colander.String(),
        missing=None
    )
