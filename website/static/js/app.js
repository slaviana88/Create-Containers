  $(function() {
    $('.show-content').on('click', function() {
      var $container = $(this).parent('.content-container'),
          $content = $container.find('.content'),
          $hideButton = $container.find('.hide-content');

      $(this).addClass('hidden');
      $content.removeClass('hidden');
      $hideButton.removeClass('hidden');
    });

    $('.hide-content').on('click', function() {
      var $container = $(this).parent('.content-container'),
          $content = $container.find('.content'),
          $showButton = $container.find('.show-content');

      $(this).addClass('hidden');
      $content.addClass('hidden');
      $showButton.removeClass('hidden');
    });
  });