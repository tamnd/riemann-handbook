---
id: term-ex
title: Matched global test functions for one Hecke monomial
kind: theorem
decl: UpperTheory.ConvolutionTheory.GM.termEx
module: Development.AutomorphicArithmetic.Foundations.Convolution.GeneralizedMeasures.TermEx
covers: 966
status: drafted
drafted_by: writer@claude
---
This theorem is the first step of [global matching from the unit](/entry/gm-of-unit/). From the local matching of the units ($\mathrm{LocUnit}$), it makes matched global test functions over $E$ and $F$ for one monomial in the Hecke operators, with the constant $\kappa_0 \prod_{v \in S} c_v$. Its main inputs are [`G.g4`](/entry/g4/) and [`locAll`](/entry/loc-all/). Names follow the parent entry.

## Statement

**Theorem.** $\mathrm{LocUnit}$ implies $\mathrm{TermEx}$.

$\mathrm{TermEx}$ fixes the data of $\mathrm{GM}$, with a place $q_0$ of $F$ over $q$ as well. Then there is $\kappa_0 > 0$ such that for each local datum $L$, each good $\nu$ and sides $\mathfrak{e}$, $\mathfrak{f}$ built from them, there is $Y_0 \geq 1$ with this property. For each finite set $\kappa$ of places of $E$ outside $\mathfrak{e}.S$, multisets $t_0(w)$ of $n$ nonzero numbers for $w \in \kappa$, and each $D$, there is a polynomial $\gamma$ in the variables $(w, i)$, $w \in \kappa$, $i < n$, with $\gamma(e_{i+1}(t_0(w))) \neq 0$. For each monomial $x^\beta$ in these variables of degree at most $D$ there is $Y_1 \geq 1$ such that for all evaluations of the Hecke variables, each $j$ and each word $\mathrm{wd}$ in the archimedean letters there are $f_E$, $f_F$ with:

1. $R(f_E) = A \circ \mathrm{ev}(\gamma x^\beta m(\mathrm{wd})) \circ U_q^j \circ R(g)$ with $A$, $g$, $U_q$ from $\mathfrak{e}$, and likewise for $f_F$ with the base changed polynomial;
2. the support conditions `Sup` (not unfolded here) at $w_0$ and $q_0$ with the bound $Y_1 Y_0^{|\mathrm{wd}|}$;
3. $f_E$ and $f_F$ match globally (`GMatch`) with constant $\kappa_0 \prod_{v \in L.S} c_v$.

## Proof

1. **The constant.** `G.g4` gives $k > 0$ and `locQ` gives $c_q > 0$. Put $\kappa_0 = k\, c_\infty\, c_q$.
2. **The sides.** `termE` and `termF` give $Y_E$, $Y_F$; put $Y_0 = \max(Y_E, Y_F)$.
3. **The polynomial.** The places of $\kappa$ lie over places outside $L.S \cup \{q\}$, which are unramified. `locAll` gives $\gamma_w$ for each $w \in \kappa$. Put $\gamma = \prod_{w \in \kappa} \gamma_w$, each in its own variables.
4. **The local functions.** Split $x^\beta$ into one polynomial $p_w$ for each $w$ (`mono_split`). `sphEx` gives spherical $h_w$ with Satake transform $\gamma_w p_w$ and $f_v$ on $F$ with transform $\prod_{w \mid v} \gamma_w p_w$ under $x \mapsto x^{f(w)}$, $f(w)$ the residue degree.
5. **Assembly.** At $v \in L.S$ use the data of $L$. At $q$ use the Iwahori functions of $j\nu$, which match with $c_q$ by `locQ`. At every other $v$ use $\bigotimes_{w \mid v} h_w$ and $f_v$ (units when no $w \mid v$ is in $\kappa$), which match with constant 1 by `locAll`. Then `G.g4` gives the global matching. The rest is bookkeeping.

## In the Lean code

The theorem is in [TermEx.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/TermEx.lean#L125), with `maxHeartbeats 1000000`. $\mathrm{TermEx}$ is in [HeckeFinAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/GeneralizedMeasures/HeckeFinAlt.lean#L154).

- $\mathrm{LocUnit}$ is used only through `locAll`, at every place outside $L.S \cup \{q\}$ (line 251).
- The constant $\kappa_0$ does not depend on $L$, $\nu$ or $\kappa$.
