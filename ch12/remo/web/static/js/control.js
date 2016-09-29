var RemoControl = function() {
    this.execute = function(remo_id, btn_id){
        $.ajax({
            method: "GET",
            url: '/remo/' + remo_id + '/' + btn_id + '/execute'
        })
            .done(function( msg ) {
                console.log( "resp: " + JSON.stringify(msg) );
            });
    };
};


$('document').ready(function(){
    window.remo_control = new RemoControl();
});

