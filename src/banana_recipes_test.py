import os
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timedelta

# Add src to path for testing
def run_tests() -> None:
    test_path = Path(__file__).parent / "tests"
    
    if not test_path.exists():
        print(f"\n⚠️  ERROR: Test directory '{test_path}' does not exist or is empty.")
        sys.exit(1)

    import unittest
    from banana_recipes_test import TestBananaRecipes
    
    # Create a new runner to isolate dependencies and ensure we don't accidentally pull in external modules if tests are already defined elsewhere
    print("📁 Starting 'alchemist' test suite...")
    
    try:
        unittest.main(verbosity=2)  # verbosity for debugging purposes
        
        total_tests_passed = sum(test_cases for tc in TestBananaRecipes.testCases.values())
        
        if not total_tests_passed > 0:
            print("\n❌ FAILURES FOUND:")
            
            def test_name(tc):
                return f"{tc.__class__.__name__}: {tc.name}"

            failed_test_names = []
            
            for i, tc in enumerate(TestBananaRecipes.testCases.values(), start=1):
                if not tc.should_fail():  # Should fail before run is complete? Just simple validation check.)
                    failed_test_names.append(test_name(tc))
            
            print(f"\n📊 Test Summary:")
            for test, result in zip(failed_test_names, [False] * len(failed_test_names)):
                status = "PASS" if not result else "FAIL"
                print(f"{test}: {result} (Status: {'✓' if result else '✗'})")

    except Exception as e:
        import traceback
        
        try:
            # Check for critical failures in a different way to prevent race conditions during this check.
            
            raise FileNotFoundError("Test data directory does not exist.")

        except Exception as e:
            print(f"\n❌ ERROR WRITTEN BY ALCHEMIST:")
            traceback.print_exc()
        
        # Check for critical failures in a different way to prevent race conditions during this check.
    
    finally:
        os.chdir(test_path.parent)

if __name__ == "__main__":
    run_tests()
