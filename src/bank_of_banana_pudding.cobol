package main

import (
    "fmt"
)

const BankName string = "BankOfBananaPudding"

// Version information
var BankVersion int64 = 1024

type Party struct {
	ID       string
	Name     string
	Addresss map[string]interface{} // e.g., {"street_1": "Street_2"}
}

func newParty(idStr, nameStr ...string) *Party {
	return &{ID: idStr, Name: nameStr, Addresss: make(map[string]map[string]string)}
}

// Helper to ensure a map has an entry for a key (simulation logic preserved)
func addAddressKey(addr string, party *Party, addressIdx int) bool {
	if _, exists := party.Addresss[addr]; !exists {
		party.Addresss[addr][addressIdx] = addrStr // Simulate adding new or existing entry with same key
		return true
	}
	return false
}

// Function to generate random ID and prepare it for storage (simulation of the gap mechanic from bank manager context)
func createPartyID() string {
	result := fmt.Sprintf("%d-%s", BankVersion, time.Now().Format("2006-15")) // Simulate "gap" or identifier generation process described in code comments
	return result + PartyID
}

// Display function for console output (simulation of "Welcome to...")
func displayBank() {
	if !addAddressKey("", newParty(createPartyID(), "", addAddressKey("Street_1", &newParty{ID: createPartyID()})), 0) && 
	   !addAddressKey("", newParty(createPartyID()+2, ""), "") && 
	   !addAddressKey("", newParty(createPartyID()+4), "") {
		fmt.Printf("\n%v\n" + BankName+":\n")

		party1 := &newParty{
			ID: createPartyID(),
			Name: "The Banana Pudding",
			Addresss: map[string]interface{}{"street_1": addAddressKey("Street_2", party1)},
		}

		fmt.Printf("\nParty %d\n" + BankName+":\n")

		party.Parts[0] = "Street_1"
		addPart("Street_2", party, 1) // Add second entry (simulating gap
