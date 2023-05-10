<template>
  <div class="team">
    <div class="team-max">
      <div class="team-introduce">
        <div class="team-block-title">
          <h2 class="team-title" v-html="this.team.title"></h2>
          <div class="team-description" v-html="this.team.description"></div>
        </div>

        <div class="team-head-staff">
          <div class="team-staff" v-if="this.staffArr.length > 0">
            <div class="team-staff-image" v-if="this.staffArr[0].image !== null">
              <img
                  :src="`${this.backendURL}${this.staffArr[0].image}`"
                  :alt="`${this.staffArr[0].name} - ${this.staffArr[0].post}`"
              >
            </div>
            <div v-else class="team-staff-no-image">
              <img
                  src="/icons/icon-photo.svg"
                  :alt="`${this.staffArr[0].name} - ${this.staffArr[0].post}`"
              >
            </div>
            <h3 class="team-staff-title" v-html="this.staffArr[0].name"></h3>
            <div class="team-staff-post" v-html="this.staffArr[0].post"></div>
          </div>

          <div class="team-staff" v-if="this.staffArr.length > 0">
            <div class="team-staff-image" v-if="this.staffArr[1].image !== null">
              <img
                  :src="`${this.backendURL}${this.staffArr[1].image}`"
                  :alt="`${this.staffArr[1].name} - ${this.staffArr[1].post}`"
              >
            </div>
            <div v-else class="team-staff-no-image">
              <img
                  src="/icons/icon-photo.svg"
                  :alt="`${this.staffArr[1].name} - ${this.staffArr[1].post}`"
              >
            </div>
            <h3 class="team-staff-title" v-html="this.staffArr[1].name"></h3>
            <div class="team-staff-post" v-html="this.staffArr[1].post"></div>
          </div>
        </div>
      </div>

      <div class="team-grid" v-if="this.staffArr.slice(2).length > 0">
        <div class="team-staff" v-for="staff in this.staffArr.slice(2)">
            <div class="team-staff-image" v-if="staff.image !== null">
              <img
                  :src="`${this.backendURL}${staff.image}`"
                  :alt="`${staff.name} - ${staff.post}`"
              >
            </div>
            <div v-else class="team-staff-no-image">
              <img
                  src="/icons/icon-photo.svg"
                  :alt="`${staff.name} - ${staff.post}`"
              >
            </div>
            <h3 class="team-staff-title" v-html="staff.name"></h3>
            <div class="team-staff-post" v-html="staff.post"></div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Team",
  inject: ['backendURL'],
  props: [
    'team',
    'staffArr',
  ],
}
</script>

<style scoped>
.team{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 75px;
  padding-bottom: 75px;
}

.team-max{
  max-width: 67rem;
  margin: 0 2rem;
}

.team-introduce{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.team-block-title{
  width: 50%;
  flex-basis: 50%;
}

.team-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 30px;
}

.team-description{
  width: 80%;
  color: #000000;
  line-height: 1.4;
  font-size: 16px;
}

.team-head-staff{
  width: 50%;
  flex-basis: 50%;
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.team-staff{
  /*height: 400px;*/
  width: 100%;
}

.team-staff-image{
  border-radius: 30px;
  /*height: 350px;*/
  width: 100%;
}

.team-staff-image img{
  width: 100%;
  border-radius: 30px;
  object-fit: cover;
  height: 350px;
}

.team-staff-no-image{
  background: #ECECEC;
  border-radius: 30px;
  height: 350px;
  width: 100%;
  position: relative;
}

.team-staff-no-image img{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.team-staff-title{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  padding-top: 20px;
  line-height: 31px;
}

.team-staff-post{
  color: #686868;
  font-size: 16px;
  line-height: 1.4;
  padding-top: 5px;
}

.team-grid{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 60px 16px;
  margin-bottom: 150px;
  padding-top: 60px;
}

@media screen and (max-width: 990px){
  .team-introduce{
    flex-direction: column;
  }

  .team-block-title{
    width: 100%;
    flex-basis: 100%;
  }

  .team-head-staff{
    width: 100%;
    flex-basis: 100%;
  }

  .team-staff-image img{
    height: 500px;
  }

  .team-staff-no-image{
    height: 500px;
  }

  .team-grid{
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 640px){
  .team{
    max-width: 100%;
    margin: 0 2rem;
    width: auto;
  }

  .team-max{
    max-width: 100%;
    margin: 0;
  }

  .team-title{
    line-height: 38px;
    font-size: 30px;
  }

  .team-staff-image img{
    height: 250px;
  }

  .team-staff-no-image{
    height: 250px;
  }
}

@media screen and (max-width: 360px){

}
</style>