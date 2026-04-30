<template>
  <div class="stat-grid">
    <div v-for="card in cards" :key="card.label" class="stat-card">
      <div class="stat-accent" :style="{ background: card.color }"></div>
      <div class="stat-body">
        <span class="stat-value">{{ card.value }}</span>
        <span class="stat-label">{{ card.label }}</span>
      </div>
      <div class="stat-icon" :style="{ color: card.color }">
        <slot :name="card.label.toLowerCase()" />
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  cards: {
    type: Array,
    required: true,
  },
})
</script>

<style scoped>
.stat-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 1px 3px 0 rgb(0 0 0/.1);
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 0;
  overflow: hidden;
  transition: box-shadow .15s, transform .15s;
}

.stat-card:hover {
  box-shadow: 0 4px 12px rgb(0 0 0/.1);
  transform: translateY(-1px);
}

.stat-accent {
  width: 4px;
  align-self: stretch;
  flex-shrink: 0;
  border-radius: 0;
}

.stat-body {
  display: flex;
  flex-direction: column;
  padding: 18px 16px 18px 0;
  flex: 1;
}

.stat-value {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -1px;
  color: #0f172a;
  line-height: 1;
}

.stat-label {
  font-size: 12px;
  font-weight: 500;
  color: #64748b;
  margin-top: 4px;
  text-transform: uppercase;
  letter-spacing: .05em;
}
</style>
