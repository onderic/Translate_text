

<template>
  <div class="max-w-md mx-auto bg-gray-300 mt-10 rounded-md px-8 py-8">
    <form @submit.prevent="translateText" class="text-center">
      <h1 class="mb-6 font-bold text-2xl">Translate here</h1>
      <div class="mb-4">
        <label for="text" class="text-gray-800">Text:</label>
        <textarea v-model="text" name="text" id="text" cols="20" rows="5" required class="border border-gray-300 rounded-md p-4 w-full"></textarea>
      </div>
      <div class="mb-4">
          <label for="language" class="text-gray-800">Translate To:</label>
          <select id="language" v-model="language" required class="border border-gray-300 p-2 w-full">
            <option value="sw">Kiswahili</option>
            <option value="en">English</option>
            <option value="fr">French</option>
            <option value="es">Spanish</option>
            <option value="de">German</option>
            <option value="it">Italian</option>
            <option value="pt">Portuguese</option>
            <option value="nl">Dutch</option>
            <option value="ru">Russian</option>
            <option value="ja">Japanese</option>
            <option value="ko">Korean</option>
            <option value="zh-CN">Chinese (Simplified)</option>
            <option value="ar">Arabic</option>
            <option value="hi">Hindi</option>
            <option value="tr">Turkish</option>
            <option value="vi">Vietnamese</option>
            <!-- Add more language options as needed -->
          </select>
    </div>
      <div>
        <button :disabled="isTranslating" class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit">
          <template v-if="isTranslating">
            Translating<span class="animate-ping mr-2 ">...</span>
          </template>
          <template v-else>
            Submit
          </template>
        </button>
      </div>
    </form>
    <div v-if="translatedText" class="mt-8 bg-gray-100 p-4 rounded-md text-center">
      <h2 class="text-lg font-semibold">Translated Text:</h2>
      <p class="text-gray-800">{{ translatedText }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      text: '',
      language: 'sw', // Set the default language to 'sw' (Kiswahili)
      translatedText: '',
      isTranslating: false
    };
  },
  methods: {
    translateText() {
      this.isTranslating = true;
      
      // Make an API call to the backend to translate the text
      // Replace 'YOUR_BACKEND_URL' with the actual URL of your backend API
      axios.post('/api/v1/translate/', { translate: this.text, language: this.language })
        .then(response => {
          this.translatedText = response.data.translation;
          this.isTranslating = false;
        })
        .catch(error => {
          console.error(error);
          this.isTranslating = false;
        });
    }
  }
};
</script>
