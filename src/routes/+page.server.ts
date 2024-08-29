import axios from "axios";

export const load = async ({ fetch,locals, cookies }:any) => {
  const turnos = await axios.get('https://rto-backend-nestjs.onrender.com/turnos')

  return {
    turnos: turnos.data.data || [],
  }
}