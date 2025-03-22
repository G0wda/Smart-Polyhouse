/*
  # Create motor status table and functions

  1. New Tables
    - `motor_status`
      - `id` (uuid, primary key)
      - `plant_id` (integer, references plants)
      - `is_running` (boolean)
      - `last_updated` (timestamp)

  2. Functions
    - `toggle_motor` function to update motor status
    
  3. Security
    - Enable RLS on `motor_status` table
    - Add policies for authenticated users
*/

CREATE TABLE IF NOT EXISTS motor_status (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  plant_id integer NOT NULL,
  is_running boolean DEFAULT false,
  last_updated timestamptz DEFAULT now()
);

ALTER TABLE motor_status ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read motor status"
  ON motor_status
  FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "Users can update motor status"
  ON motor_status
  FOR UPDATE
  TO authenticated
  USING (true)
  WITH CHECK (true);

-- Function to toggle motor status
CREATE OR REPLACE FUNCTION toggle_motor(p_plant_id integer, p_status boolean)
RETURNS motor_status AS $$
DECLARE
  motor motor_status;
BEGIN
  INSERT INTO motor_status (plant_id, is_running)
  VALUES (p_plant_id, p_status)
  ON CONFLICT (plant_id) DO UPDATE
    SET is_running = p_status,
        last_updated = now()
  RETURNING * INTO motor;
  
  RETURN motor;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;