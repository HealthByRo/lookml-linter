from typing import Union
from linter.helpers import snake_case_to_pascal_case
from linter.rule import ParamSet, Rule, Severity

# TODO: AUTO-IMPORT RULES
from linter.rules.field_requires_description import FieldRequiresDescription
from linter.rules.view_with_many_fields_requires_fields_hidden_by_default import (
    ViewWithManyFieldsRequiresFieldsHiddenByDefault,
)
from linter.rules.view_with_dimensions_and_measures_has_one_primary_key import (
    ViewWithDimensionsAndMeasuresHasOnePrimaryKey,
)
from linter.rules.dimension_group_of_type_time_requires_datatype import (
    DimensionGroupOfTypeTimeRequiresDatatype,
)
from linter.rules.dimension_group_of_type_time_requires_timeframe import (
    DimensionGroupOfTypeTimeRequiresTimeframe,
)
from linter.rules.explore_requires_description import ExploreRequiresDescription
from linter.rules.explore_joins_require_relationship import (
    ExploreJoinsRequireRelationship,
)

# this rule may be used in the future for partial matching. another option is regex matching.
from linter.rules.explore_joins_contain_many_to_many_relationship import (
    ExploreJoinsContainManyToManyRelationship,
)
from linter.rules.field_match_to_required_access_grant import (
    FieldMatchToRequiredAccessGrant,
)


class RuleFactory:
    def __init__(self) -> None:
        pass

    def build(
        self, rule_name: str, severity: Severity, params: Union[ParamSet, None] = None
    ) -> Rule:
        classname = snake_case_to_pascal_case(rule_name)
        return globals()[classname](severity, params)
