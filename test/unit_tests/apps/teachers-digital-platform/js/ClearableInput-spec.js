import { ClearableInput } from '../../../../../cfgov/unprocessed/apps/teachers-digital-platform/js/ClearableInput.js';
import { simulateEvent } from '../../../../util/simulate-event.js';

let baseDom;
let clearBtnDom;
let inputDom;

const HTML_SNIPPET = `
<div class="o-form--input-w-btn__input-container">
     <div class="m-btn-inside-input
                 input-contains-label">
         <label for="query" class="input-contains-label__before
                                   input-contains-label__before--search">
         </label>
         <label for="query" class="input-contains-label__after
                                   input-contains-label__after--clear">
         </label>
         <input type="text"
                title="Search the CFPB"
                class="a-text-input"
                value=""
                placeholder="Search the CFPB">
     </div>
</div>
`;

describe('ClearableInput', () => {
  beforeEach(() => {
    document.body.innerHTML = HTML_SNIPPET;
    baseDom = document.querySelector('.o-form--input-w-btn__input-container');
    inputDom = baseDom.querySelector('input');
    clearBtnDom = baseDom.querySelector('.input-contains-label__after--clear');
  });

  describe('init function', () => {
    it('should hide the clear button when a value is empty', () => {
      new ClearableInput(baseDom).init();
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(true);
    });

    it('should display the clear button when a value is present', () => {
      inputDom.value = 'testing init function';
      new ClearableInput(baseDom).init();
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(false);
    });
  });

  describe('on clear button click', () => {
    it('should hide itself', () => {
      inputDom.value = 'testing clear button';
      new ClearableInput(baseDom).init();
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(false);
      simulateEvent('mousedown', clearBtnDom);
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(true);
    });

    it('should clear the input value', () => {
      inputDom.value = 'testing clear button';
      new ClearableInput(baseDom).init();
      simulateEvent('mousedown', clearBtnDom);
      expect(inputDom.value).toStrictEqual('');
    });
  });

  describe('on input keystroke', () => {
    it('should show the clear button, if value present', () => {
      new ClearableInput(baseDom).init();

      simulateEvent('keyup', inputDom, { key: 'a' });
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(false);
    });

    it('should hide the clear button, if value not present', () => {
      new ClearableInput(baseDom).init();

      simulateEvent('keyup', inputDom, { key: 'a' });
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(false);
      simulateEvent('keyup', inputDom, { key: 'Backspace' });
      expect(clearBtnDom.classList.contains('u-hidden')).toStrictEqual(true);
    });
  });
});
