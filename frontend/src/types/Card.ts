export interface Card {
  id: number;
  front: string;
  back: string;
  repetitions: number;
  createdAt: Date;
  updatedAt: Date;
  labels: string[];
}
