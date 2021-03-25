const NOT_FOUND = -1
const BODY_ELEMENT = document.querySelector('body')
const filterForm = document.querySelector("form[data-filter-form='']");

if (filterForm !== null) {
    var baseFilter = {
        init: function () {
            this.table = document.querySelector("tbody[data-filter-target='']");
            console.log(this.table)
            this.rows = this.table.children;
            console.log(this.rows)
            return this;
        },
        checkDropdownExact: function(selectId, targetId){
            return function(description){
                let selected = document.getElementById(selectId).value;
                let target = description.getElementsByClassName(targetId)[0];
                return target.innerHTML === selected || selected === "all";
            }
        },
        checkTextInput: function (inputId, targetId) {
            return function (description) {
                let input = document.getElementById(inputId);
                let target = description.getElementsByClassName(targetId)[0];
                let sanitizedInput = sanitizeString(input.value);
                console.log(sanitizedInput);
                return (target && sanitizeString(target.innerHTML).indexOf(sanitizedInput) > -1) || sanitizedInput === '';
            }
        },
        filter: function (description_container='property_description') {
            for (i = 0; i < this.rows.length; i++) {
                if (this.evaluations.every((evaluate) => evaluate(this.rows[i]))) {
                    this.rows[i].style.display = "";
                }
                else {
                    this.rows[i].style.display = "none";
                }
            }
        }
    }.init();

    var ownerFilter = {
        ...baseFilter,
        evaluations: [
            baseFilter.checkTextInput('search_owner', 'owner_name'),
            baseFilter.checkTextInput('search_owner_id', 'owner_id'),
        ]
    }
    var propertyFilter = {
        ...baseFilter,
        evaluations: [
            baseFilter.checkDropdownExact('search_property_type', 'property_type'),
            baseFilter.checkTextInput('search_catastral', 'property_catastral_id'),
            baseFilter.checkTextInput('search_address', 'property_address'),
        ]
    }
    console.log(`owner ${JSON.stringify(ownerFilter)}`)

    let queryParams = window.location.search.substr(1);
    console.log(`QPARAMS ${JSON.stringify(queryParams)}`)

    if (queryParams) {
        console.log(`TRUE QPARAMS ${JSON.stringify(queryParams)}`)
        console.log(`TRUE QPARAMS ${queryParams}`)
        window.addEventListener('load', applyFilterFromQueryParams(queryParams));
    }

    function sanitizeString(string) {
        string = string.toUpperCase();
        string = string.normalize('NFD').replace(/[\u0300-\u036f]/g, "");
        return string.trim();
    }


    function applyFilterFromQueryParams(query) {
        if (query) {
            let [targetFilterField, value] = getQueryParamsComponents(query);
            let inputElement = getInputElement(targetFilterField);
            setElementValueFromQueryParam(inputElement, value);
            triggerEventOnElement(inputElement);
        }
    };

    function getQueryParamsComponents(query) {
        return query.split('=');
    }

    function getInputElement(targetFilterField) {
        return document.querySelector(`#${targetFilterField}`);
    }

    function setElementValueFromQueryParam(element, value) {
        element.value = decodeURIComponent(value.replace(/\+/g, ' '));
    }

    function triggerEventOnElement(element) {
        if (element.type === 'text') {
            element.onkeyup();
        }
        else {
            element.onchange();
        }
    }

}