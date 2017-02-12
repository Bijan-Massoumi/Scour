//
//  WindowViewController.swift
//  Scour
//
//  Created by Bijan Massoumi on 12/17/16.
//  Copyright © 2016 Bijan Massoum. All rights reserved.
//

import Cocoa

class WindowViewController: NSViewController {
    @IBOutlet weak var emailField: NSTextField!
    @IBOutlet weak var searchTerms: NSTextField!
    @IBOutlet weak var minPrice: NSTextField!
    @IBOutlet weak var maxPrice: NSTextField!
    @IBOutlet weak var furnitureBool: NSButton!
    @IBOutlet weak var freeBool: NSButton!
    @IBOutlet weak var submitButton: NSButton!

    override func viewDidLoad() {        
        super.viewDidLoad()
        // Do view setup here.
    }
    
    
}
