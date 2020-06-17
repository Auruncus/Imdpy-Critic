$(document).ready(function() {
    var box = PUBNUB.$('chat');
    var input = PUBNUB.$('input');
    var channel = 'simple_chat';
    
    var name = "Anonymous"
    
    input.focus();
    
    PUBNUB.subscribe({
      channel: channel,
      callback: function(text) {
        box.innerHTML = '<li>' + ('' + text).replace(/[<>]/g, '') + box.innerHTML + '</li>';
      }
    });
    
    PUBNUB.bind('keyup', input, function(e) {
      (e.keyCode || e.charCode) == 13 && input.value.length > 0 && input.value !== " " && PUBNUB.publish({
        channel: channel,
        message: name + " says: " + input.value,
        x: (input.value = '')
      });
    });
  });