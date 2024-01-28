export interface Card {
  id: number;
  front: string;
  back: string;
  labels: string[];
  next_review: number;
  user_id: number;
  repeat_count: number;
}
