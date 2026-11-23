---
title: A moduli point over a finite normal extension
decls:
  - GlobalTheory.ArcPoint.exists_point
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A moduli point over a finite normal extension

Let $a$ be an arc over an arc base $(O', \varpi)$. In this section we prove that there are a finite, injective and integrally closed extension $R_1$ of $O'[[X]]$ and a point $y_1$ of the moduli space $X_{o,F}$ over $\operatorname{Frac} R_1$ with two properties. At each test point with $|X| < 1$, the point $y_1$ is Mumford's uniformisation of $a$ with parameter $X$. Over an algebraic closure of $\operatorname{Frac} R_1$, its theta points of level $n^j$ are integral families. The point is built from one object with full level over the algebraic closure $K$ of $\operatorname{Frac} O'[[X]]$, whose theta points are the series of [the first section](/entry/exists-arc-series-integral-algebraic-over-power-series/), through [the theta points at one level](/entry/exists-full-theta/). The result is the first step of [the arc family theorem](/entry/arc-fam/).

### Points of the moduli space with full level

We keep the notation of the first three sections. The level $l$ has integers $A, M$ and an ideal $\mathfrak{m}$, and the model $Y$ carries a universal semi-abelian scheme $G$ with level points $\eta_A$ of level $A$ and $\eta$ of level $M$. Let $K_A$ be the field generated over $\mathbb{Q}$ by $\rho_{\mathbb{C}}$ and $\zeta_A$, with its constants $\rho$ and $\zeta$.

**Definition 6.4.1 (Full level at a point).** Let $K$ be a field, let $y : \operatorname{Spec} K \to X_{o,F}$ and let $o$ be an object with full level over $K$. We say that $o$ *lies at* $y$ if there is a map $\varphi : A(o) \to G$ that makes $A(o)$ the pullback of $G$ along $y$, with these properties: $L(o)$ is isomorphic to the pullback of the polarization bundle of $G$; $\varphi$ commutes with the actions of $\mathcal{O}_E$; $\varphi \circ \operatorname{ev}_A(v) = \eta_A(v) \circ y$ for all $v$; $\varphi \circ \operatorname{ev}_M(v) = \eta(v) \circ y$ for $v$ in $\bar{\mathfrak{m}} \Lambda$; and for each map $f : K_A \to K$ under which $y$ lies over $f$, we have $\rho(o) = f(\rho)$ and $\zeta_A(o) = f(\zeta)$.

**Definition 6.4.2 (Extension of objects).** Let $f : K \to K'$ be a field map and let $o, o'$ be objects with full level over $K$ and $K'$. Then $o'$ *extends* $o$ along $f$ if $\rho(o') = f(\rho(o))$, $\zeta_n(o') = f(\zeta_n(o))$ for all $n$, and there is a map $A(o') \to A(o)$ that makes $A(o')$ the pullback of $A(o)$ along $f$ and matches the line bundles, the actions of $\mathcal{O}_E$ and the maps $\operatorname{ev}_n$.

**Definition 6.4.3 (Arc point).** Let $R_1$ be a domain, $g : O'[[X]] \to R_1$ a ring map and $y_1 : \operatorname{Spec} \operatorname{Frac} R_1 \to X_{o,F}$. The pair $(g, y_1)$ is an *arc point* if $g$ is injective and finite and $y_1$, followed by $j : X_{o,F} \to Y$ and the structure map to $\operatorname{Spec} V$, is the map given by $V \xrightarrow{b} O' \to O'[[X]] \xrightarrow{g} R_1 \to \operatorname{Frac} R_1$.

**Definition 6.4.4 (Realised arc point).** An arc point $(g, y_1)$ *realises* the arc $a$ if, at each test point $(C, \gamma)$ of $\operatorname{Frac} R_1$ with $u = \gamma(g(X))$, there are an integral lift $A'$ of $a$ to $C$, a system of roots $r$ of $u$, and an object $o$ with full level over $C$ that lies at $y_1 \circ \gamma$, such that $o$ *realises* $A'$ with parameter $u$ and roots $r$. This means: $\rho(o) = \rho(A')$ and $\zeta_n(o) = \zeta_n(A')$ for all $n$; for each odd $m$ and each family $p$ of classes that are twist-related to $q_{m^2}$ by $r(m^2)$, the theta terms are summable and $x \mapsto \vartheta_m(p(x))$ is a theta point of $o$ of level $m$; and the same holds for the coordinates at each $\operatorname{ev}_j(z)$.

Here a test point of $\operatorname{Frac} R_1$ is defined as for $K$ in the first section, with $i$ replaced by $O'[[X]] \to R_1 \to \operatorname{Frac} R_1$.

**Definition 6.4.5 (Integral theta points).** An arc point $(g, y_1)$ has *integral theta points* if there is an object $o$ with full level over an algebraic closure $\bar K_1$ of $\operatorname{Frac} R_1$ that lies at $y_1$, such that for each odd prime $n$ that is a unit in $O'$ and each $j \geq 1$ there is a theta point $v$ of $o$ of level $n^j$ that is an integral family for $(g(X), R_1 \to \bar K_1, n^{j-1})$.

### Inputs on the moduli space

We use four results of the Lean development that this chapter does not prove. Each assumes the seven inputs.

**Theorem 6.4.6 (Moduli points of objects).** Let $K$ be an algebraically closed field and $b_F : F \to K$ a field map. Every object $o$ over $K$ whose constants $\rho$ and $\zeta_A$ are the images under $b_F$ of the elements of $F$ that go to $\rho_{\mathbb{C}}$ and $\zeta_A$ lies at a unique point $y$ of $X_{o,F}$ over $b_F$. Every point $y$ over $K$ has an object that lies at it. If $o$ lies at $y$ and $o'$ extends $o$ along $f : K \to K'$, then $o'$ lies at $y \circ f$.

Lean: `GlobalTheory.T.fullTorsionObject_existsUnique_moduliPoint`.

**Theorem 6.4.7 (Extension to a larger closed field).** Let $f : K \to K'$ be a map of algebraically closed fields of characteristic $0$. Each object $o$ over $K$ has an extension $o'$ along $f$, and $f$ carries the theta points and the coordinates of $o$ to those of $o'$.

Lean: `GlobalTheory.T.fullTorsionPolarizedCMObject_extends_algClosed`.

**Theorem 6.4.8 (All prime power levels).** Let $S$ be a series datum in $K$ and $n$ an odd prime. If for each $j \geq 2$ there is an object with the constants of $S$ and theta point $v_{n^j}$ of level $n^j$, then there is one object $o_0$ with $\rho(o_0) = \rho(S)$ such that, for all $j$, $\zeta_{n^j}(o_0) = \zeta_{n^j}(S)$ and $v_{n^j}$ is a theta point of $o_0$ of level $n^j$.

Lean: `GlobalTheory.T.thetaPoints_allPrimePowerLevels_of_single_object`.

**Theorem 6.4.9 (Compatibility with the series).** Let $S$ be a series datum in $K$ and $n$ an odd prime that is a unit in $O'$. If $o_0$ is an object as in the conclusion of the previous theorem, then there is an object $o$ over $K$ that has the constants of $S$ and, for every odd $m$, theta point $v_m$ of level $m$ and coordinates $w_{m,j,z}$ at each $\operatorname{ev}_j(z)$. We say that $o$ *carries* $S$.

Lean: `GlobalTheory.T.power_series_algebraic_closure_compatible`.

### The theorem

**Theorem 6.4.10 (Moduli point of an arc).** Assume the seven inputs. Let $Y$ be a model of $X_o$, let $(O', \varpi)$ be an arc base with $O'$ of characteristic $0$, let $b : V \to O'$ and let $a$ be an arc over $(O', b)$. Then there are an integrally closed domain $R_1$, an injective and finite map $g : O'[[X]] \to R_1$, and a point $y_1$ of $X_{o,F}$ over $\operatorname{Frac} R_1$, such that $(g, y_1)$ is an arc point that realises $a$ and has integral theta points.

Lean: `GlobalTheory.ArcPoint.exists_point`.

*Proof.* Since $(O', \varpi)$ is an arc base, $O'$ is local and principal, so $O'[[X]]$ is a noetherian, integrally closed domain of characteristic $0$. Let $K_0 = \operatorname{Frac} O'[[X]]$ and let $K$ be an algebraic closure of $K_0$. Then $K$ satisfies the hypotheses of the theorem on series of theta values, and we get a series datum $S$ in $K$.

Since $O'$ is local and $d \neq 0$, there is an odd prime $n$ that is a unit in $O'$ with $n \nmid d$. Indeed, take two distinct primes $p, q \geq d + 3$. They are coprime, so $ap + bq = 1$ in $O'$ for some $a, b$, and in a local ring one of $ap$ and $bq$ is a unit. So $p$ or $q$ is a unit in $O'$, and it is odd and does not divide $d$. By the theorem on theta points of a series datum, for each $j \geq 2$ there is an object over $K$ with theta point $v_{n^j}$. The theorem on all prime power levels gives one object $o_0$ for all $j$, and the theorem on compatibility with the series gives an object $o$ over $K$ that carries $S$.

The field $F$ is a number field and $V$ is a valuation ring of $F$, so the map $V \to O' \to K_0$ extends to a field map $b_F : F \to K_0$. The constants of $o$ are those of $S$, which are the images of $\rho_{\mathbb{C}}$ and $\zeta_A$ under $b$, since $S$ has a lift of $a$. Here we use that an element $r \in F$ with $r^2 = -d$, or with $r^A = 1$, lies in $V$. By the theorem on moduli points, $o$ lies at a unique point $y : \operatorname{Spec} K \to X_{o,F}$ over $b_F$.

The moduli space is of finite type over $F$, so $y$ factors through a field $L$ that is finite over $K_0$. Let $R_1$ be the integral closure of $O'[[X]]$ in $L$. It is a domain, finite over $O'[[X]]$ since $O'[[X]]$ is noetherian of characteristic $0$, and integrally closed, with $\operatorname{Frac} R_1 = L$. Let $g$ be the inclusion and $y_1$ the point over $L$. The compatibility of $y_1$ with $b$ follows from the construction of $b_F$, so $(g, y_1)$ is an arc point.

For each algebraically closed field $C$ and each map $\gamma : \operatorname{Frac} R_1 \to C$, the map $\gamma$ extends to $f : K \to C$, since $K$ is algebraic over $L$. Then $y \circ f = y_1 \circ \gamma$ and $f$ agrees with $\gamma \circ g$ on $O'[[X]]$.

*The arc point realises $a$.* Let $(C, \gamma)$ be a test point of $\operatorname{Frac} R_1$ and $f$ as above. Then $(C, f)$ is a test point of $K$. Since $o$ carries $S$, the second property of the series datum gives an integral lift $A'$ of $a$ to $C$, roots $r$ of $u$ and an object $o'$ over $C$ that extends $o$ along $f$ and realises $A'$. By the last part of the theorem on moduli points, $o'$ lies at $y \circ f = y_1 \circ \gamma$.

*The theta points are integral.* Apply the construction above to $C = \bar K_1$ and the inclusion of $\operatorname{Frac} R_1$. The theorem on extension to a larger closed field gives an extension $o'$ of $o$ along $f$, and $o'$ lies at $y_1$. For $n$ and $j \geq 1$ as in the definition, $v_{n^j}$ is a theta point of $o$, so $f \circ v_{n^j}$ is a theta point of $o'$. The family $v_{n^j}$ is integral for $(X, K, n^{j-1})$ by the first property of the series datum. Let $S'$ be a valuation ring of $\bar K_1$ that contains $R_1$. Then $f^{-1}(S')$ is a valuation ring of $K$ that contains $O'[[X]]$, and $f$ preserves the valuation $1$. So $f \circ v_{n^j}$ is integral for $(g(X), R_1 \to \bar K_1, n^{j-1})$. $\square$

**Remark 6.4.11 (Formalization).** The Lean proof is in [ExistsExtendValuation.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsExtendValuation.lean#L180). The four inputs on the moduli space are statements of the development proved outside this chapter, and we did not unfold their proofs. The step from an object that carries $S$ to a realisation at a test point is the lemma `realises_of_has` (same file, line 146). The transfer of integral families is `intFam_map` (same file, line 171). In the theorem on moduli points only the first and third parts are used; the second part is discarded. We did not unfold `IsGrpPullback`, `LBIso` or `Model`.
