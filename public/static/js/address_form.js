const display_address_form = () => {
    const selected_type = document.querySelector('#id_type');
    const urban_form = document.querySelector('#urban');
    const rural_form = document.querySelector('#rural');

    if (selected_type.value === "1") {
        urban_form.style.display = "";
        rural_form.style.display = "none";
    } else {
        urban_form.style.display = "none";
        rural_form.style.display = "";
    }
}
display_address_form();