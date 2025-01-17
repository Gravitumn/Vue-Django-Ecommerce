<template>
  <div>
    <select @change="toggleOption($event)" multiple>
      <option
        v-for="option in options"
        :key="option.id"
        :value="JSON.stringify(option)"
        :style="{ color: isSelected(option) ? 'gray' : 'black' }"
      >
        {{ option.name }}
      </option>
    </select>
    <p>
      Selected Options:
      <input type="text" :value="formattedSelectedOptions" readonly />
    </p>
  </div>
</template>

<script>

export default {
  data() {
    return {
      selectedOptions: [], // Array of selected JSON objects
    };
  },
  props: {
    options: {
      type: Array,
      required: true,
    },
  },
  computed: {
    formattedSelectedOptions() {
      const count = this.selectedOptions.length;
      if (count === 0) return "None";
      if (count === 1) return this.selectedOptions[0].name;
      if (count === 2)
        return `${this.selectedOptions[0].name} , ${this.selectedOptions[1].name}`;
      if (count === 3)
        return this.selectedOptions.map((option) => option.name).join(", ");
      return `There is ${count} more...`;
    },
  },
  methods: {
      toggleOption(event) {
        const selectedOption = JSON.parse(event.target.value);
        const exists = this.selectedOptions.find(opt => opt.id === selectedOption.id);
  
        if (exists) {
          // Remove if already selected
          this.selectedOptions = this.selectedOptions.filter(opt => opt.id !== selectedOption.id);
        } else {
          // Add if not already selected
          this.selectedOptions = [...this.selectedOptions, selectedOption];
        }
      },
      isSelected(option) {
        return this.selectedOptions.some(opt => opt.id === option.id);
      },
    },
    watch:{
      selectedOptions:{
        deep:true,
        handler(newVal){
          this.$emit("update:categories",newVal);
        }
      }
    }
};
</script>
