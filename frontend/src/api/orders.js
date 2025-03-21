import axios from "axios";
import { API_BASE_URL } from "./config";

export const getOrders = async (userId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/orders?user_id=${userId}`);
    return response.data;
  } catch (error) {
    console.error("Errore nel recupero degli ordini:", error.response?.data || error.message);
    alert("Errore nel recupero degli ordini. Riprova più tardi.");
    throw error;
  }
};