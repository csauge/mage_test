if 'extension' not in globals():
    from mage_ai.data_preparation.decorators import extension


@extension('great_expectations')
def validate(validator, *args, **kwargs):
    validator.expect_table_row_count_to_be_between(
        min_value=1400,
    )
    validator.expect_table_columns_to_match_set(
        column_set=[
            'station_id',
            'name',
            'lat',
            'lon',
            'capacity',
        ],
        exact_match=False,
    )