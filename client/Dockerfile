FROM node:lts

WORKDIR /client

COPY ./package*.json ./

RUN npm install

COPY . .

ENV PORT=3000
ENV HOST=0.0.0.0

EXPOSE 3000

RUN npm run build

CMD ["npm", "run", "start"]