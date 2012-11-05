/* -*- Mode: C; tab-width: 8; indent-tabs-mode: nil; c-basic-offset: 4 -*-
 *
 * ***** BEGIN LICENSE BLOCK *****
 * Version: MPL 1.1/GPL 2.0/LGPL 2.1
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * The Original Code is Mozilla Communicator client code, released
 * March 31, 1998.
 *
 * The Initial Developer of the Original Code is
 * Netscape Communications Corporation.
 * Portions created by the Initial Developer are Copyright (C) 1998
 * the Initial Developer. All Rights Reserved.
 *
 * Contributor(s):
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either of the GNU General Public License Version 2 or later (the "GPL"),
 * or the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *
 * ***** END LICENSE BLOCK ***** */

/*
 * JS document package.
 */
#include "jsstddef.h"
#include "jslibmath.h"
#include <stdlib.h>
#include "jstypes.h"
#include "jslong.h"
#include "prmjtime.h"
#include "jsapi.h"
#include "jsatom.h"
#include "jscntxt.h"
#include "jsconfig.h"
#include "jslock.h"
#include "jsmath.h"
#include "jsdocument.h"
#include "jsnum.h"
#include "jsobj.h"

#define WRITELOG "write.log"
#define WRITEUCLOG "write.uc.log"

static JSClass document_class = {
    "document",
    0,
    JS_PropertyStub,  JS_PropertyStub,  JS_PropertyStub,  JS_PropertyStub,
    JS_EnumerateStub, JS_ResolveStub,   JS_ConvertStub,   JS_FinalizeStub,
    JSCLASS_NO_OPTIONAL_MEMBERS
};

static JSBool
document_write(JSContext *cx, JSObject *obj, uintN argc, jsval *argv, jsval *rval)
{
    JSString *str;
    size_t n, i;
    jschar *s;
    FILE *fOut, *fOutUC;

    str = js_ValueToString(cx, argv[0]);
    if (!str)
        return JS_FALSE;

    if (JSSTRING_IS_DEPENDENT(str)) {
        n = JSSTRDEP_LENGTH(str);
        s = JSSTRDEP_CHARS(str);
    } else {
        n = str->length;
        s = str->chars;
    }

    if ((fOutUC = fopen(WRITEUCLOG, "r")) == NULL)
    {
        fOutUC = fopen(WRITEUCLOG, "w");
        fputc(0xFF, fOutUC);
        fputc(0xFE, fOutUC);
        fclose(fOutUC);
    }

    fOutUC = fopen(WRITEUCLOG, "a");
    if (fOutUC == NULL)
        return JS_FALSE;

    fwrite(s, n, 2, fOutUC);

    fclose (fOutUC);

    fOut = fopen(WRITELOG, "a");
    if (fOut == NULL)
        return JS_FALSE;

    for (i = 0; i < n; i++)
        fputc(s[i], fOut);

    fclose (fOut);

    return JS_TRUE;
}

#if JS_HAS_TOSOURCE
static JSBool
document_toSource(JSContext *cx, JSObject *obj, uintN argc, jsval *argv,
	      jsval *rval)
{
    *rval = ATOM_KEY(cx->runtime->atomState.DocumentAtom);
    return JS_TRUE;
}
#endif

static JSFunctionSpec document_static_methods[] = {
#if JS_HAS_TOSOURCE
    {js_toSource_str,   document_toSource,		0, 0, 0},
#endif
    {"write",		document_write,		1, 0, 0},
    {0,0,0,0,0}
};

JSObject *
js_InitDocumentClass(JSContext *cx, JSObject *obj)
{
    JSObject *Document;
    
    Document = JS_DefineObject(cx, obj, "document", &document_class, NULL, 0);
    if (!Document)
        return NULL;
    if (!JS_DefineFunctions(cx, Document, document_static_methods))
        return NULL;

    return Document;
}
