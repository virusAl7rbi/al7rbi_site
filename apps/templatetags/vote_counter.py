from django import template

register = template.Library()


def total_votes(votes):
    votes_up = sum([x.vote_up for x in votes if x.vote_up == 1])
    votes_down = sum([x.vote_down for x in votes if x.vote_down == 1])
    return votes_up - votes_down


register.filter('total_votes',total_votes)