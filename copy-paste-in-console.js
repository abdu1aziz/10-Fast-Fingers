var word_idx = 0;
var interval_per_word = 250; // in milliseconds
function hackit(){
    if(word_idx<words.length){
        $('#inputfield').val(words[word_idx] + ' ');
        var keyup = jQuery.Event('keyup');
        keyup.which = 32;
        $('#inputfield').trigger(keyup);
        word_idx++;
        setTimeout('hackit()', interval_per_word);
    }
}
setTimeout('hackit()', interval_per_word);