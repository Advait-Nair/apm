/*
 * Carousel class for constructing interactive carousel/sliders
*/

/* 
    %%%apm%%%

    name:: Carousel.js
    description:: A JavaScript class for constructing interactive carousel/sliders.
    iteration:: 14
    author:: Advait Nair

    %%%apm%%%
*/


class Carousel {
    constructor (carousel, indicator) {
        this.target = carousel;
        if(!this.target) return;
        this.carouselItems = this.target.querySelectorAll('.carousel-item');
        this.indicator = indicator;
        this.carouselPosition = 0;
        this.fallingBack = 0 // What direction is carousel cycling in
        this.shift = 1;
        this.interacting = false;
        this.createBottomBar();
        setTimeout(() => {
            this.target.classList.add('animated');
        }, 5000)
    }

    init (time) {
        this.carouselItems.forEach((element, index) => {
            element.style = `transform: translateX(${((index+this.shift)*100)-100}vw)`;
		});

        this.refreshBottomBar();

        // setInterval(() => {
        //     this.nextFrame();
        // }, time || 5000)
        this.cycle(time);

        const prev = this.target.parentElement.querySelector('.carousel-controller .prev');
        const next = this.target.parentElement.querySelector('.carousel-controller .next');

        next.addEventListener('click', e => {this.nextFrame(); this.interacting = true});
        prev.addEventListener('click', e => {this.previousFrame(); this.interacting = true});
    }
    createBottomBar() {
        this.indicator.innerHTML = '';
        this.carouselItems.forEach((element, index) => {
            const dot = document.createElement('div');
            dot.addEventListener('click', e => {
                this.interacting = true;
                this.carouselItems.forEach((element, index) => {
					if(
                        this.indicator
						.querySelector(`.dot:nth-child(${index + 1})`) === dot
                    ) {
                        this.carouselPosition = index - 1;
                        this.nextFrame();
                    }
				});
            })
            dot.classList.add('dot');
            if (index === this.carouselPosition)
            dot.classList.add('active');
            this.indicator.appendChild(dot);
        });
    }
    refreshBottomBar() {
        this.carouselItems.forEach((element, index) => {
            this.indicator.querySelector(`.dot:nth-child(${index+1})`).classList.remove('active');
            if (index === this.carouselPosition) {
                this.indicator.querySelector(`.dot:nth-child(${index+1})`).classList.add('active');
            }
        });
    }
    nextFrame(reset) {
        if(this.carouselPosition === this.carouselItems.length-1) {
            this.fallingBack = true;
            if(reset) this.carouselPosition = -1;
            return;
        }

        let shift = this.shift;
        let movement = -1 - this.carouselPosition;
        
        this.carouselItems.forEach((element, index) => {
            let styling = `transform: translateX(${((index+shift+movement)*100)-100}vw)`;
            element.style = styling;
        });
        this.carouselPosition++;
        this.refreshBottomBar();
    }
    previousFrame() {
        if(this.carouselPosition === 0) {this.fallingBack=false;return;}

        let shift = this.shift;
        let movement = -this.carouselPosition;
        if(this.carouselPosition == 1) {
            movement = -1 + this.carouselPosition;
        }
        
        this.carouselItems.forEach((element, index) => {
            let styling = `transform: translateX(${((index+shift+movement)*100)-100}vw)`;
            console.log(styling)
            element.style = styling;
        });
        this.carouselPosition--;
        this.refreshBottomBar();
    }

    cycle (time) {
        // if(this.carouselPosition == 0){
        //     this.fallingBack = false;
        //     this.nextFrame();
        // }
        // if(this.carouselPosition == this.carouselItems.length-1) {
        //     this.fallingBack = true;
        //     this.previousFrame();
        // }

        // if(this.fallingBack) this.previousFrame();
        // else this.nextFrame();

        // setTimeout(() => this.cycle(), time)
        // this.carouselItems.forEach(element => {
        //     setTimeout(()=> {
        //         this.nextFrame();
        //     }, time)
        // })
        // this.carouselItems.forEach(element => {
        //     setTimeout(()=> {
        //         this.previousFrame();
        //     }, time)
        // })
        setInterval(() => {
            if(this.interacting) {this.interacting = false; return;}
            this.nextFrame(true);

        }, time)
    }
}