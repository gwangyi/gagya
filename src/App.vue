<template>
  <div id="app">
    <div class="controlpanel">
      <vue-multi-select
        v-model="selectedConsonantParts"
        search
        historyButton
        :btnLabel="() => '자음'"
        :options="options"
        :filters="consonantFilters"
        labelValue="value"
        :selectOptions="allConsonants"
      >
        <template v-slot:option="{ option }">
          <input type="checkbox" :checked="option.selected" />
          <span>{{ option.name }}</span>
        </template>
      </vue-multi-select>
      <vue-multi-select
        v-model="selectedVowelParts"
        search
        historyButton
        :btnLabel="() => '모음'"
        :options="options"
        :filters="vowelFilters"
        labelValue="value"
        :selectOptions="allVowels"
      >
        <template v-slot:option="{ option }">
          <input type="checkbox" :checked="option.selected" />
          <span>{{ option.name }}</span>
        </template>
      </vue-multi-select>
      <select v-model="jongseong">
        <option value="">(받침없음)</option>
        <option v-for="(j, i) in jongseongs" :key="i" :value="j">
          {{ hangulLetterMap[j] }}
        </option>
      </select>
    </div>
    <div class="row">
      <GlyphCell />
      <GlyphCell v-for="(v, i) in vowels" :key="i" :cell="v" />
    </div>
    <div class="row" v-for="(c, i) in consonants" :key="i">
      <GlyphCell :cell="c" />
      <GlyphCell
        v-for="(v, j) in vowelParts"
        :key="j"
        :cell="consonantParts[i] + v + jongseong"
        :type="type"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import vueMultiSelect from "vue-multi-select";
import "vue-multi-select/dist/lib/vue-multi-select.css";
import GlyphCell from "./components/GlyphCell.vue";
import { hangulLetterMap } from "./lettermap";

// Both end are inclusive
const charRange = (start: number, end: number) =>
  [...Array(end - start + 1).keys()].map((i) => String.fromCharCode(i + start));

const CHOSEONG = charRange(0x1100, 0x1112);
const JUNGSEONG = charRange(0x1161, 0x1175);
const JONGSEONG = charRange(0x11a8, 0x11bf);
const BASIC_CONSONANTS = [
  "\u3131", // KIYEOK
  "\u3134", // NIEUN
  "\u3137", // TIKEUT
  "\u3139", // RIEUL
  "\u3141", // MIEUM
  "\u3142", // PIEUP
  "\u3145", // SIOS
  "\u3147", // IEUNG
  "\u3148", // CIEUC
  "\u314a", // CHIEUCH
  "\u314b", // KHIEUKH
  "\u314c", // THIEUTH
  "\u314d", // PHIEUPH
  "\u314e", // HIEUH
];
const BASIC_VOWELS = [
  "\u314f", // A
  "\u3151", // YA
  "\u3153", // EO
  "\u3155", // YEO
  "\u3157", // O
  "\u315b", // YO
  "\u315c", // U
  "\u3160", // YU
  "\u3161", // EU
  "\u3163", // I
];

@Component({
  components: {
    GlyphCell,
    vueMultiSelect,
  },
})
export default class App extends Vue {
  // For templates, only field of Vue object can be used in the template.
  private hangulLetterMap = hangulLetterMap;
  private options = {
    multi: true,
  };
  private consonantFilters = [
    {
      nameAll: "기본 자모",
      nameNotAll: "기본 자모",
      func({ name }: { name: string }) {
        return BASIC_CONSONANTS.includes(name);
      },
    },
    {
      nameAll: "전반",
      nameNotAll: "전반",
      func({ value }: { value: string }) {
        return CHOSEONG.indexOf(value) < CHOSEONG.length / 2;
      },
    },
    {
      nameAll: "후반",
      nameNotAll: "후반",
      func({ value }: { value: string }) {
        return CHOSEONG.indexOf(value) >= CHOSEONG.length / 2;
      },
    },
  ];
  private vowelFilters = [
    {
      nameAll: "기본 자모",
      nameNotAll: "기본 자모",
      func({ name }: { name: string }) {
        return BASIC_VOWELS.includes(name);
      },
    },
    {
      nameAll: "전반",
      nameNotAll: "전반",
      func({ value }: { value: string }) {
        return JUNGSEONG.indexOf(value) < JUNGSEONG.length / 2;
      },
    },
    {
      nameAll: "후반",
      nameNotAll: "후반",
      func({ value }: { value: string }) {
        return JUNGSEONG.indexOf(value) >= JUNGSEONG.length / 2;
      },
    },
  ];
  private allVowels = JUNGSEONG.map((ch) => ({
    name: hangulLetterMap[ch],
    value: ch,
  }));
  private allConsonants = CHOSEONG.map((ch) => ({
    name: hangulLetterMap[ch],
    value: ch,
  }));
  private jongseongs = JONGSEONG;
  private jongseong = "";

  private selectedVowelParts = JUNGSEONG.map((ch) => ({
    name: hangulLetterMap[ch],
    value: ch,
  })).filter(({ name }) => BASIC_VOWELS.includes(name));
  private selectedConsonantParts = CHOSEONG.map((ch) => ({
    name: hangulLetterMap[ch],
    value: ch,
  })).filter(({ name }) => BASIC_CONSONANTS.includes(name));

  private get vowels() {
    return this.selectedVowelParts.map(({ name }) => name).sort();
  }
  private get consonants() {
    return this.selectedConsonantParts.map(({ name }) => name).sort();
  }

  private get vowelParts() {
    return this.selectedVowelParts.map(({ value }) => value).sort();
  }
  private get consonantParts() {
    return this.selectedConsonantParts.map(({ value }) => value).sort();
  }
  private type = "grey";
}
</script>

<style>
#app {
  top: 6vh;
  left: 6vw;
  width: 88vw;
  height: 88vh;
  position: absolute;
  display: flex;
  flex-direction: column;
}
#app .row {
  display: flex;
  flex-direction: row;
  height: 8vw;
}
@media only print {
  #app .controlpanel {
    display: none;
  }
}
#app .row .cell {
  flex: 1;
}
</style>
