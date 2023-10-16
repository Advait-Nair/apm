
/* 
    %%%apm%%%

    name:: LithiumJS
    description:: A JavaScript library for simplifying common DOM operations.
    iteration:: 3
    author:: Advait Nair

    %%%apm%%%
*/




/**
 * 
 * @param {string} queryString
 * @returns document element object.
 * 
 * Pass in a string and get a document element object returned.
 * The string is the same kind of string you pass into a querySelector.
 * (short for querySelector)
 */
const qs = q => {
    if(!document.querySelector(q)) return;
    if(q === undefined) return;
    return document.querySelector(q);
}




/**
 * 
 * @param {string} queryString
 * @returns document element object collection.
 * 
 * Pass in a string and get every document element object of that query returned.
 * The string is the same kind of string you pass into a querySelector.
 * (Short for QuerySelectorAll)
 */
const qsa = q => {
    if(!document.querySelectorAll(q)) return;
    if(q === undefined) return;
    return document.querySelectorAll(q);
}



/**
 * 
 * @param {string} element
 * @param {string} onEvent
 * @param {function} Callback
 * 
 * AddEventListener function. Takes three parameters - element, onEvent & callback.
 * The first parameter is a querySelector string that identifies the document element to add an event listener to.
 * The second parameter is a string that describes which event will fire the callback function, e.g. "click".
 * The third parameter is the callback function that will be called when the event described on the element is triggered.
 */
const ael = (el, on, cb) => {
    if(typeof el === 'string' && !document.querySelector(el)) return;
    if(el === undefined) return;
    if(on === undefined) return;
    if(cb === undefined) return;
    
    function onExe(e) {
        cb(e)
    }
    
    
    if(typeof el === 'string' && document.querySelector(el)){
        document.querySelector(el).addEventListener(on, onExe);
    } else {
        el.addEventListener(on, onExe);
    }
    
    
    
}


/**
 * 
 * @param {string} type
 * @param {string} element
 * @param {function} function
 * 
 * RemoveEventListener function. Takes three parameters - type, element & function.
 * The first parameter is the event type that triggers the callback function, e.g. "click".
 * The second parameter is a querySelector string that identifies the document element to remove an event listener from.
 * The third parameter is the callback function that was originally passed in when the eventListener was created.
 */
const rel = (type, el, fn) => {
    if(typeof fn !== 'function') return;
    if(fn === undefined) return;
    if(el === undefined) return;
    
    document.querySelector(el).removeEventListener(type, fn);
}


/**
 * 
 * @param {string} messages
 * 
 * Log function. Logs to console. Can include multiple messages.
 */
const log = console.log


/**
 * 
 * @param {string} messages
 * 
 * Log error function. Logs error to console. Can include multiple messages.
 */
const err = console.error


/**
 * 
 * @param {string} messages
 * 
 * Warn function. Logs warning to console. Can include multiple messages.
 */
const war = console.warn




/**
 * 
 * @param {string} element
 * @param {string} content
 * 
 * Set text content of document element.
 * First parameter takes in a querySelector string to identify the target document element.
 * Second parameter takes in a content string to change the content of the element
 * 
 * (Add/Replace text content of the element)
 */
const text = (element, content) => {
    if(typeof element !== 'string') return;
    if(element === undefined) return;
    if(content === undefined) return;
    qs(element).textContent = content;
}



/**
 * 
 * @param {string} element
 * @param {string} content
 * 
 * Append text content of document element.
 * First parameter takes in a querySelector string to identify the target document element.
 * Second parameter takes in a content string to add content to the element.
 * 
 * (Adds on to end of existing text content of element, e.g. ```
 * addtext('.text','text')
 * ```)
 */
const addtext = (element, content) => {
    if(typeof element !== 'string') return;
    if(element === undefined) return;
    if(content === undefined) return;
    qs(element).textContent += content;
}



/**
 * 
 * @param {string} element
 * @param {string} content
 * 
 * Change innerHTML of document element.
 * First parameter takes in a querySelector string to identify the target document element.
 * Second parameter takes in a content string to add innerHTML to the element.
 * 
 * (Changes innerHTML of element)
 */
const inner = (element, content) => {
    if(typeof element !== 'string') return;
    if(element === undefined) return;
    if(content === undefined) return;
    qs(element).innerHTML = content;
}



/**
 * 
 * @param {string} element
 * @param {string} content
 * 
 * Adds to end of innerHTML of a  document element.
 * First parameter takes in a querySelector string to identify the target document element.
 * Second parameter takes in a content string to add innerHTML to the element.
 * 
 * (Appends innerHTML to element)
 */
const addinner = (element, content) => {
    if(typeof element !== 'string') return;
    if(element === undefined) return;
    if(content === undefined) return;
    qs(element).innerHTML += content;
}


/**
 * 
 * @param {string} element
 * @param {string} content
 * 
 * Adds to end of outerHTML of a  document element.
 * First parameter takes in a querySelector string to identify the target document element.
 * Second parameter takes in a content string to add outerHTML to the element.
 * 
 * (Appends outerHTML to element)
 */
const addouter = (element, content) => {
    if(typeof element !== 'string') return;
    if(element === undefined) return;
    if(content === undefined) return;
    qs(element).outerHTML += content;
}

/**
 * 
 * @param {string} element
 * @param {string} content
 * 
 * Change outerHTML of document element.
 * First parameter takes in a querySelector string to identify the target document element.
 * Second parameter takes in a content string to add outerHTML to the element.
 * 
 * (Changes outerHTML of element)
 */
const outer = (element, content) => {
    if(typeof element !== 'string') return;
    if(element === undefined) return;
    if(content === undefined) return;
    qs(element).outerHTML = content;
}


/**
 * 
 * @param {string} elem
 * @param {function} cb
 * 
 * Do something when an element is clicked
 * 
 * First parameter - target document element to add eventListener to
 * Second parameter - callback function that describes what to do when eventListener is fired
 */
const onclick = (elem, cb) => {
    if(typeof elem !== 'string') return;
    if(elem === undefined) return;
    if(cb === undefined) return;
    
    function onExe(e) {
        cb(e);
    }
    qs(elem).addEventListener('click', onExe)
}




/**
 * 
 * @param {string} elem
 * @param {function} cb
 * 
 * Do something when an element is being hovered on
 * 
 * First parameter - target document element to add eventListener to
 * Second parameter - callback function that describes what to do when eventListener is fired
 */
const onhover = (elem, cb) => {
    if(typeof elem !== 'string') return;
    if(elem === undefined) return;
    if(cb === undefined) return;
    
    function onExe(e) {
        cb(e);
    }
    qs(elem).addEventListener('mouseover', onExe)
    
    qs(item).outerHTML = content;
}


/**
 * 
 * @param {string} elementType
 * @param {string} content
 * @returns document element with content
 * 
 * Create new document element
 * 
 * First parameter - What kind of element to create, e.g. 'div' for <div></div>
 * Second parameter - What content will be in the element (can be text or HTML)
 * 
 * when making HTML string content, it may help to use struct().
 */
const element = (elemtype, content) => {
    if(typeof elemtype !== 'string') return;
    if(elemtype === undefined) return;
    if(content === undefined) return;
    let f = document.createElement(elemtype);
    f.innerHTML = content;
    return f;
}



/**
 * 
 * @param {documentElement} elementType
 * @param {string} insertTo
 * 
 * Inserts element into another element.
 * 
 * First parameter - Element (not a string, a document element) to insert
 * Second parameter - Element (string) to insert new element into
 * 
 * e.g.
 * ```javascript
 * const timeDisplay = element('h2', '15:07');
 * insert(timeDisplay, '.time-container');
 * ```
 * 
 */
const insert = (elem, to) => {
    if(elem === undefined) return;
    if(to === undefined) return;
    qs(to).appendChild(elem);
}



/**
 * 
 * @param {documentElement} element
 * @param {string} insertTo
 * @param {string} insertBefore
 * 
 * Inserts element into another element before a child.
 * 
 * First parameter - Element (not a string, a document element) to insert
 * Second parameter - Element (string) to insert new element into
 * Second parameter - Element (string) to insert before
 * 
 * 
 */
const insertbefore = (elem, to, before) => {
    if(elem === undefined) return;
    if(to === undefined) return;
    if(before === undefined) return;
    qs(to).insertBefore(elem, qs(before));
}


/**
 * 
 * @param {string} element
 * @param {string} classesToInsert
 * 
 * Adds classes to an element
 * 
 * First parameter - Element (string) to add class to
 * Second parameter/all other parameters - classes to insert
 * 
 * e.g.
 * ```javascript
 * addclass('.time', 'timed', 'dark', 'theme-darwin');
 * // Adds timed, dark and theme-darwin class names to the element '.time'.
 * 
 * ```
 * 
 * 
 */
const addclass = (elem, ...classes) => {
    if(elem === undefined) return;
    if(classes === undefined) return;
    if(typeof elem === 'string'){
        classes.forEach(c => qs(elem).classList.add(c))
    }
    
    else{
        classes.forEach(c => elem.classList.add(c))
    }
    
    return typeof elem === 'string' ? qs(elem) : elem
}


/**
 * 
 * @param {string} element
 * @param {string} classesToRemove
 * 
 * Removes classes to an element
 * 
 * First parameter - Element (string) to remove class from
 * Second parameter/all other parameters - classes to remove
 * 
 * e.g.
 * ```javascript
 * removeclass('.time', 'times', 'light', 'theme-win86');
 * // Adds timed, dark and theme-darwin class names to the element '.time'.
 * 
 * ```
 * 
 * 
 */
const removeclass = (elem, ...classes) => {
    if(elem === undefined) return;
    if(classes === undefined) return;
    if(typeof elem === 'string'){
        classes.forEach(c => qs(elem).classList.remove(c))
    }
    
    else{
        classes.forEach(c => elem.classList.remove(c))
    }
    
    return elem;
}




/**
 * 
 * @param {string} HTMLStruct
 * 
 * Creates HTML for you easily.
 * 
 * use this syntax to create HTML structures - 
 * 
 * elementType{elementContent}
 * elementType.classes{elementContent}
 * 
 * Note that this feature has limited capability and element content can only be text or actual HTML as you cannot recurse the syntax just yet.
 * 
 */
const struct = (HTMLStruct) => {
    if(HTMLStruct === undefined) return;
    let HTML = ''
    if(HTMLStruct.includes('{')){
        HTMLStruct.split(',').forEach(element => {
            try{
                let tag = element.split('{')[0].trim();
                content = element.split('{')[1].replace('}','');
                let classid = undefined;
                if(tag.includes('.')){
                    tag = tag.split('.');
                    classid = tag;
                    tag = tag[0]
                    classid.splice(0, 1)
                }
                
                if(classid === undefined){
                    HTML += `
                    <${tag}>${
                        struct(content)
                    }</${tag}>
                    `.trim();
                } else {
                    let classF = '';
                    classid.forEach(classItem => {
                        classF += classItem + ' ';
                    })
                    classF = classF.trim();
                    HTML += `
                    <${tag} class="${classF}">${
                        struct(content)
                    }</${tag}>
                    `.trim();
                }
                
            }catch{}
        });
    } else {
        return HTMLStruct;
    }
    return HTML;
}
/**
 * 
 * @param {string} element
 * 
 * Remove element from DOM.
 * 
 * First parameter is the element querySelector string.
 * 
 */
const remove = (elem) => {
    if(elem === undefined) return;
    qs(elem).remove();
}


/**
 * 
 * @param {string} element
 * 
 * Remove elements from DOM.
 * 
 * First parameter is the element querySelectorAll string.
 * 
 */
const removeall = (elem) => {
    if(elem === undefined) return;
    qs(elem).remove();
}



/**
 * 
 * @param {string} element
 * 
 * Remove elements from DOM.
 * 
 * First parameter is the element querySelectorAll string.
 * 
 */
const floop = (cond, cb) => {
    if(elem === undefined) return;
    qs(elem).remove();
}

