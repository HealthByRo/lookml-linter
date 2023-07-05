from linter.rule import Rule


class FieldMatchToRequiredAccessGrant(Rule):
    def applies_to():
        return ("dimension", "measure", "dimension_group")

    def run(self, field):
        # user attribute typically used with required_access_grants
        config_user_attribute = self.params["user_attribute"]
        # search terms (typically used to reference field name property) applied to each user attribute
        config_search_terms = self.params["search_terms"]
        search_pattern = " ".join(
            [field.get(key, "") for key in ["name", "label", "description"]]
        )
        # check any existing search terms are found have necessary required_access_grants property
        search_terms_match_in_name_label_description = any(
            [word == search_pattern.strip() for word in config_search_terms]
        )
        word_search_terms_match_in_name_label_description = [
            word for word in config_search_terms if word == search_pattern.strip()
        ]

        if search_terms_match_in_name_label_description:
            user_attribute_equals_required_access_grant = all(
                [
                    config_user_attribute == access_grant_in_lkml
                    for access_grant_in_lkml in field.get(
                        "required_access_grants", ["no grant"]
                    )
                ]
            )
            return user_attribute_equals_required_access_grant
        return True
