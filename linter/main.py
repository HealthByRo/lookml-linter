import os
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.rules_engine import RulesEngine
from linter.lookml_project_parser import LookMlProjectParser


def main():
    config_file = os.environ['INPUT_CONFIGFILE']
    lkml_dir = os.environ.get('INPUT_LOOKMLPROJECT', "./")

    validator = ConfigValidator(config_file)
    validator.validate()
    config = validator.config
    rules = RulesEngine(config).rules
    parser = LookMlProjectParser(lkml_dir)
    data = parser.get_parsed_lookml_files()
    linter = LookMlLinter(data, rules)
    print(f"running linter on following directory {lkml_dir}")
    linter.run()
    linter.print_errors()
    assert linter.has_errors == False, "LookML Linter detected an error warning, please resolve any error warning to complete Pull Request"


main()
