var a = 0;
  $(window).scroll(function() {
  
    var oTop = $('.counter').offset().top - window.innerHeight;
    if (a == 0 && $(window).scrollTop() > oTop) {
      $('.counter-value').each(function() {
        var $this = $(this),
          countTo = $this.attr('data-count');
        $({
          countNum: $this.text()
        }).animate({
            countNum: countTo
          },
  
          {
  
            duration: 4000,
            easing: 'swing',
            step: function() {
              $this.text(Math.floor(this.countNum));
            },
            complete: function() {
              $this.text(this.countNum);
              //alert('finished');
            }
  
          });
      });
      a = 1;
    }
  
  });

  const faders = document.querySelectorAll(".fade-in");
  const sliders = document.querySelectorAll(".slide-in");
  
  const appearOptions = {
    threshold: 0,
    rootMargin: "0px 0px -250px 0px",
  };
  
  const appearonScroll = new IntersectionObserver(function (
    entries,
    appearonScroll
  ) {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      } else {
        entry.target.classList.add("appear");
        appearonScroll.unobserve(entry.target);
      }
    });
  },
  appearOptions);
  
  faders.forEach((fader) => {
    appearonScroll.observe(fader);
  });
  
  sliders.forEach((fader) => {
    appearonScroll.observe(fader);
  });
  
  sliders.forEach((slider) => {
    appearonScroll.observe(slider);
  });