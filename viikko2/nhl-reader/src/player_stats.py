class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, country):
        country_players = self.reader.get_players()

        # based on nationality
        country_players_filtered = list(filter(
            lambda player: player.nationality == country, country_players)
            )
        
        # based on nationality and top points
        sorted_players = sorted(
            country_players_filtered, 
            key=lambda player: (player.goals + player.assists), 
            reverse=True
            )

        print("Players from", country)

        return sorted_players