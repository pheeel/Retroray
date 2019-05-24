// Get value from range filter and show it in span.
const getValueFromRange = (newVal, spanId) => {
    return (document.getElementById(spanId).innerHTML = newVal);
};