'use strict';

let request = null;

// ajax get results
function getResults(event) {
    
    event.preventDefault();

    // serialize form data from the form i.e get user inputs of filters
    let formData = $(event.target).closest('form').serialize();  // serialize automatically encodes input
    let url = '/search?' + formData;

    // abort previous request so state is up to date
    if (request != null)
        request.abort();

    request = $.ajax({
        url: url,
        type: 'GET',
        success: handleResponse,
        error: handleError
    });
}

// handle ajax response
function handleResponse(data) {
    const resultsContainer = $('.results-container');
    const searchSection = $('.search-section');
    const errorMsg = $('.error-msg');

    // pre-processing: clear error messages
    resultsContainer.empty();
    searchSection.hide();
    errorMsg.hide();

    if (data && data.response) {
        let price = data.response;
        let borderClass = '';

        if (price >= 0 && price < 17000) {
            borderClass = 'border-green';
        } else if (price >= 17000 && price < 37000) {
            borderClass = 'border-orange';
        } else if (price >= 37000) {
            borderClass = 'border-red';
        }

        let htmlContent = `<div class="results ${borderClass}">`;
        htmlContent += `<p>$${price}</p>`;
        htmlContent += '</div>';
        resultsContainer.append(htmlContent);
    } else {
        resultsContainer.append('<p>No data available.</p>');
    }

    searchSection.show();

}

function handleError(res) {
    let errorMessage = "error";
    const responseJSON = JSON.parse(res.responseText);
    if (responseJSON.error)
        errorMessage = responseJSON.error;

    $('.error-msg p').text(errorMessage);
    $('.error-msg').show();
    $('.search-section').hide();
}

// set up event listeners
function setUp() {
    $('#car-form').on('submit', getResults);
}

$(document).ready(setUp);
