//
//  PXGlass.h
//  cocoaglass
//
//  Created by Simhadri on 10/15/13.
//  Copyright (c) 2013 Moji, Inc. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface PXGlass : NSObject

+(NSString*)exportPreview:(NSString*)srcPath;
+(NSString*)exportPreview:(NSString*)srcPath maxWidth:(float)width maxHeight:(float)height;
+(NSString*)exportPreview:(NSString*)srcPath maxWidth:(float)width maxHeight:(float)height inFormat:(NSString*)format;

@end
