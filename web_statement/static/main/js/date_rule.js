"use strict";
if ((document.getElementById("persistent_rule_hidden").value == 'True') || $('#persistent_rule').is(':checked'))
    {
    $('#date_rule_start_label').hide(100);
    $('#date_rule_end_label').hide(100);
    $("#persistent_rule").attr("checked","checked");
    }
    else
    {
    $("#persistent_rule").removeAttr("checked");
    }
$('#persistent_rule').click(function(){
    if ($(this).is(':checked'))
        {
        $('#date_rule_start_label').hide(100);
        $('#date_rule_end_label').hide(100);
        $('#date_rule_end').attr('value', '');
        $('#date_rule_start').attr('value', '');
        }
        else
        {
        $('#date_rule_start_label').show(100);
        $('#date_rule_end_label').show(100);
        }
});