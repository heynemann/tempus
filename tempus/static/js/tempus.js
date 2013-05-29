var tempus = function(element, time) {
    this.element = element;
    this.time = time;
    this.startTime = null;
};

tempus.prototype = {
    start: function() {
        this.startTime = new Date();
        this.boundRender = this.render.bind(this);
        window.requestAnimationFrame(this.boundRender);
    },
    render: function(timestamp) {
        var dt = new Date();
        var diff = (dt - this.startTime) / 1000;
        var count = Math.ceil(this.time - diff);
        if (count < 0) {
            count = 0;
        }
        this.element.html(count);

        if (count > 0) {
            window.requestAnimFrame(this.boundRender);
        } else {
            this.reset();
        }
    },
    reset: function() {
        this.startTime = null;
        this.element.html('YAY!');
    }
};
