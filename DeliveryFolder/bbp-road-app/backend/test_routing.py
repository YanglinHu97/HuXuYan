#!/usr/bin/env python
"""Test the new routing algorithm."""
import httpx
import json

def test_routing():
    response = httpx.post(
        'http://127.0.0.1:8000/api/path/search',
        json={
            'origin': {'lat': 45.4642, 'lon': 9.1900},
            'destination': {'lat': 45.4784, 'lon': 9.2275},
            'preferences': 'safety_first'
        },
        timeout=30.0
    )
    data = response.json()
    
    print("=" * 60)
    print("ROUTE SEARCH TEST RESULTS")
    print("=" * 60)
    print(f"Route Source: {data.get('route_source')}")
    print(f"Algorithm: {data.get('algorithm')}")
    print(f"Candidates Generated: {data.get('candidates_generated')}")
    print(f"Candidates Returned: {data.get('candidates_returned')}")
    print()
    
    for route in data.get('routes', []):
        print(f"Route {route['route_id']} (Rank {route['rank']}):")
        print(f"  Distance: {route['total_distance']}m")
        print(f"  Duration: {route['duration_display']}")
        print(f"  Quality Score: {route['road_quality_score']}")
        print(f"  Tags: {route['tags']}")
        print(f"  Source: {route['source']}")
        print()
    
    print("=" * 60)
    print("Testing different preferences...")
    print("=" * 60)
    
    for pref in ['shortest', 'balanced']:
        response = httpx.post(
            'http://127.0.0.1:8000/api/path/search',
            json={
                'origin': {'lat': 45.4642, 'lon': 9.1900},
                'destination': {'lat': 45.4784, 'lon': 9.2275},
                'preferences': pref
            },
            timeout=30.0
        )
        data = response.json()
        print(f"\nPreference: {pref}")
        for route in data.get('routes', []):
            print(f"  Route {route['route_id']}: {route['total_distance']}m, Quality: {route['road_quality_score']}, Tags: {route['tags']}")

if __name__ == '__main__':
    test_routing()
