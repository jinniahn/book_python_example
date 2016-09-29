var Player = function() {
    this.play = function(){
        $.ajax({
            method: "POST",
            url: "/jukebox/control/play",
            data: {}
        })
            .done(function( msg ) {
                console.log( "resp: " + msg );
            });

    };
    this.stop = function() {
        $.ajax({
            method: "POST",
            url: "/jukebox/control/stop",
            data: {}
        })
            .done(function( msg ) {
                console.log( "resp: " + msg );
            });
    };
    this.next = function() {
        $.ajax({
            method: "POST",
            url: "/jukebox/control/next",
            data: {}
        })
            .done(function( msg ) {
                console.log( "resp: " + msg );
            });
    };

    this.add_url = function(url, add_playlist) {
        $.ajax({
            method: "POST",
            dataType: 'json',
            url: "/jukebox/songs",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({url: url, add_playlist: add_playlist})
        })
            .done(function( msg ) {
                console.log( "resp: " + msg );
            });
    };

    this.add_list_url = function(url, add_playlist) {
        $.ajax({
            method: "POST",
            dataType: 'json',
            url: "/jukebox/songs",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({list_url: url, add_playlist: add_playlist})
        })
            .done(function( msg ) {
                console.log( "resp: " + msg );
            });
    };    

    this.add_song_from_db = function(dbid) {
        $.ajax({
            method: "POST",
            dataType: 'json',
            url: "/jukebox/playlist",
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({dbid: dbid})
        })
            .done(function( msg ) {
                console.log( "resp: " + msg );
            });        
    };

    this.get_current_song = function(cb) {
        $.ajax({
            method: "GET",
            dataType: 'json',
            url: "/jukebox/current_song",
            contentType: 'application/json; charset=utf-8'
        })
            .done(function( msg ) {
                console.log( "resp: " + JSON.stringify(msg) );
                if( msg.song && cb ) {
                    cb(msg.song);
                }
            });                
    };

};


$('document').ready(function(){
    window.player = new Player();
});
