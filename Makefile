# Makefile

.NOTPARALLEL:

help:
	@echo "Syntax: make TARGETS ... [OPTIONS ...]"
	@echo "Targets:"
	@echo "  clean      cleanup old test results"
	@echo "  models     update test models"
	@echo "  validate   perform validation tests"
	@echo "Options:"
	@echo "  LIMIT='timeout TIME'"
	@echo "  VERBOSE=yes"

OPTIONS=
ifeq ($(VERBOSE),yes)
OPTIONS += --debug
endif

TEMPLATES=$(foreach ORG,$(shell grep -v ^\# .orgs),$(shell find $(ORG) -type d -print -prune))
TESTDIR=autotest/models/gridlabd-4
TESTFILES=$(foreach GLM,$(shell find $(TESTDIR) -name '*.glm' -print),$(TESTDIR)/$(GLM))

validate: clean models $(TESTFILES)
	@cat validate.txt

clean:
	@rm -rf test validate.txt

models:
	@git submodule sync
	@git submodule update --init --recursive

$(TESTDIR)/%.glm: %.glm
	@$(foreach TEMPLATE,$(TEMPLATES),$(LIMIT) ./validate.sh $(OPTIONS) "$<" "$(TEMPLATE)") >> validate.txt
