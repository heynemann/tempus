var tempus = function(element, time, onStop) {
    this.element = element;
    this.time = time;
    this.startTime = null;
    this.onStop = onStop;
};

tempus.prototype = {
    start: function() {
        this.startTime = new Date();
        this.boundRender = this.render.bind(this);
        window.requestAnimFrame(this.boundRender);
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
            if (this.onStop) {
                this.onStop(count);
            }
            this.reset();
        }
    },
    reset: function() {
        if (this.onStop) {
            var dt = new Date();
            var diff = (dt - this.startTime) / 1000;
            var count = Math.ceil(this.time - diff);

            this.onStop(count);
        }

        this.startTime = null;
        this.element.html('YAY!');
    }
};
