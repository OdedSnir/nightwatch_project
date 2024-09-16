
$(document).ready(function() {
        $("#id_brigade").change(function() {
            let brigadeId = $(this).val();

            // Load Companies based on Brigade
            let urlCompanies = '/ajax/load-companies/';
            $.ajax({
                url: urlCompanies,
                data: {
                    'brigade_id': brigadeId
                },
                success: function(data) {
                    $("#id_company").html('<option value="">---------</option>');
                    $.each(data, function(key, value) {
                        $("#id_company").append('<option value="' + value.id + '">' + value.letter + '</option>');
                    });
                    $("#id_platoon").html('<option value="">---------</option>');  // Reset platoon dropdown
                    $("#id_team").html('<option value="">---------</option>');  // Reset team dropdown
                }
            });

            // Reset platoon and team when brigade changes
            $("#id_platoon").html('<option value="">---------</option>');
            $("#id_team").html('<option value="">---------</option>');
        });

        $("#id_company").change(function() {
            let companyId = $(this).val();

            // Load Platoons based on Company
            let urlPlatoons = "/ajax/load-platoons/";
            $.ajax({
                url: urlPlatoons,
                data: {
                    'company_id': companyId
                },
                success: function(data) {
                    $("#id_platoon").html('<option value="">---------</option>');
                    $.each(data, function(key, value) {
                        $("#id_platoon").append('<option value="' + value.id + '">' + value.letter + '</option>');
                    });
                    $("#id_team").html('<option value="">---------</option>');  // Reset team dropdown
                }
            });
        });

    $("#id_platoon").change(function() {
        let platoonId = $(this).val();

        // Load Teams based on Platoon
        var urlTeams = "/ajax/load-teams/";
        $.ajax({
            url: urlTeams,
            data: {
                'platoon_id': platoonId
            },
            success: function(data) {
                $("#id_team").html('<option value="">---------</option>');
                $.each(data, function(key, value) {
                    $("#id_team").append('<option value="' + value.id + '">' + value.letter + '</option>');
                });
            }
        });
    });
});
