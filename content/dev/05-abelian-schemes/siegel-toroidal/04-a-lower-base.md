---
title: A lower base for a trait
decls:
  - GlobalTheory.T.exists_lower_base_of_trait_abelian_part
  - GlobalTheory.TChart.exists_lowBase_of_trait
  - GlobalTheory.T.siegelFibrePower_point_lifts_to_lower_base
  - GlobalTheory.LowLift.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A lower base for a trait

Near a boundary point of the compactification, the degenerating abelian scheme is built by Mumford's construction from an abelian scheme of smaller dimension, its *abelian part*, together with points on it. The charts must see this abelian part over a fixed complete local ring that is étale over a fibre power of the universal abelian scheme. We call such a ring with its data a *lower base*. This section proves that each polarized abelian scheme over a complete discrete valuation ring, with an additive family of points, comes from a lower base after a finite extension of the ring. The result is used in the next section, to write degeneration data along a trait in terms of a lower base. The main input is the étale local root of the [previous section](/entry/exists-rig-lb-s-fam-etale/).

Throughout, a *CN domain* is a noetherian, integrally closed, $\mathfrak{m}$-adically complete local domain of characteristic $0$, and $n \ge 3$ is odd. Let $F$ be a Siegel family of genus $h$ and level $n$ over $\Lambda_n$, with base $X$ and universal datum $(A, P, \ell)$. For $r \ge 0$ let $A^r$ be the $r$-fold fibre power of $A$ over $X$, with coordinate maps $\mathrm{pr}_i : A^r \to A$. If $v : T \to A^r$ is a map, then $A_v$ denotes the pullback of $A$ along $T \to A^r \to X$, $P_v$ the pullback of $P$ to $A_v \times_T A_v$, and
$$c_v(a) = \sum_{i=1}^{r} a_i \, \mathrm{pr}_i(v) \in A_v(T), \qquad a \in \mathbb{Z}^r.$$

**Definition 9.4.1 (Polarized abelian scheme).** A *polarized abelian scheme* over $S$ is an abelian scheme $A \to S$, smooth of relative dimension $g$, with a line bundle $L$ on $A$ that is rigidified, symmetric and relatively ample, and has trivial $K$-group.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.PolAV`.

**Definition 9.4.2 (Tautological base).** Let $o$ be a ring and $W$ a local ring. A *tautological base* over $W$ consists of a ring map $b : o \to W$, an abelian scheme $B$ over $W$ of relative dimension $g$, a rigidified line bundle $M$ on $B$ with a cubical structure that is relatively ample and has trivial $K$-group, an integer $r \ge 0$, an additive map $c_0 : \mathbb{Z}^r \to B(W)$, and for $a, a' \in \mathbb{Z}^r$ a generator $\tau_0(a, a')$ of the fibre at $(c_0(a), c_0(a'))$ of the inverse of the Mumford bundle $\Lambda(M)$. The $\tau_0$ are symmetric in $a, a'$, and additive in $a$ up to the cubical structure.

Lean: `GlobalTheory.PolDeg.TautBase`.

This is Mumford data over $W$, as in the [main section](/entry/siegel-toroidal-integral-holds/), but with the periods $\tau_0$ defined over $W$ itself and not only over its fraction field.

**Definition 9.4.3 (Lower base).** A *lower base* of level $n$ over $(o, \zeta)$ consists of:

1. an integer $h$ and a Siegel family $F$ of genus $h$ and level $n$ over $(o, \zeta)$;
2. a noetherian, $\mathfrak{m}$-adically complete local ring $W$ and a tautological base $T = (b, B, M, r, c_0, \tau_0)$ over $W$ with $g = h$;
3. a map $u : \operatorname{Spec} W \to A^r$ with $s \circ u = \operatorname{Spec} b$, such that the map from the local ring of $A^r$ at the image of the closed point to $W$ is flat, sends the maximal ideal onto the maximal ideal, and gives a finite, formally unramified extension of residue fields;
4. a map $\beta : B \to A$ that makes $B$ the group pullback of $A$ along $\operatorname{Spec} W \to A^r \to X$, with $\Lambda(M) \cong (\beta \times \beta)^* P$, and with $\beta \circ c_0(e_i) = \mathrm{pr}_i \circ u$ for the standard basis vectors $e_i$.

Lean: `GlobalTheory.TChart.LowBase`.

So $W$ is, up to a finite étale extension, the completed local ring of $A^r$ at a point, and the points $c_0(e_i)$ are the coordinates of that point.

**Theorem 9.4.4 (Points of a fibre power lift to a lower base).** Let $F$ be a Siegel family of genus $h$ and level $n$ over $\Lambda_n$, let $r \ge 0$, let $V_1$ be a CN domain that is a discrete valuation ring, and let $v : \operatorname{Spec} V_1 \to A^r$ lie over a map $b_1 : \Lambda_n \to V_1$. Then there are a lower base $L$ of level $n$ over $\Lambda_n$, with ring $W$, tautological base $T = (b, B, M, r_T, c_0, \tau_0)$ and $h_L = h$, a discrete valuation ring $V'$ that is a CN domain, an injective, finite, local map $f : V_1 \to V'$, a local map $\kappa : W \to V'$ with $\kappa \circ b = f \circ b_1$, and an isomorphism $e : \mathbb{Z}^{r_T} \to \mathbb{Z}^r$ with the following properties. There are a group scheme $B'$ over $V'$ and maps $\beta' : B' \to A_v$ and $\beta'' : B' \to B$ that make $B'$ the group pullback of $A_v$ along $\operatorname{Spec} f$ and of $B$ along $\operatorname{Spec} \kappa$, such that
$$(\beta' \times \beta')^* P_v \cong (\beta'' \times \beta'')^* \Lambda(M),$$
and for each $a \in \mathbb{Z}^{r_T}$ there is a section $x \in B'(V')$ with $\beta'(x) = c_v(n \, e(a))$ over $\operatorname{Spec} f$ and $\beta''(x) = c_0(n a)$ over $\operatorname{Spec}\kappa$.

Lean: `GlobalTheory.LowLift.main` (also `GlobalTheory.T.siegelFibrePower_point_lifts_to_lower_base`, a wrapper).

*Proof.* Let $w \in A^r$ be the image of the closed point of $V_1$, and let $W_0$ be the completion of the local ring of $A^r$ at $w$. It is noetherian and complete. Since $v$ sends the closed point to $w$, it factors as $\operatorname{Spec} V_1 \to \operatorname{Spec} W_0 \to A^r$ through a local map $\psi : W_0 \to V_1$.

Apply the theorem on the [étale local root](/entry/exists-rig-lb-s-fam-etale/) to $F$ and to $\operatorname{Spec} W_0 \to A^r \to X$. It gives a complete local ring $W$ and a local, injective, finite, étale map $\rho : W_0 \to W$, a group pullback $\beta : B \to A$ along $\operatorname{Spec} W \to A^r \to X$, and a rigidified cubical line bundle $M$ on $B$ that is relatively ample, has trivial $K$-group, and satisfies $\Lambda(M) \cong (\beta \times \beta)^* P$. Then $W$ is noetherian, since it is finite over $W_0$.

Let $u : \operatorname{Spec} W \to \operatorname{Spec} W_0 \to A^r$. For each $i$, the map $\mathrm{pr}_i \circ u$ and the identity of $\operatorname{Spec} W$ define, by the pullback property of $B$, a section $p_i \in B(W)$ with $\beta(p_i) = \mathrm{pr}_i \circ u$. Put $c_0(a) = \sum_i a_i p_i$; it is additive. Since $M$ is cubical, there are generators $\tau_0(a, a')$ of the inverse Mumford bundle at $(c_0(a), c_0(a'))$ that are symmetric and additive up to the cubical structure. The group scheme $B$ is smooth, proper and geometrically connected, being a pullback of $A$, so it is an abelian scheme; its relative dimension is $h$. With $b = \rho \circ b_0$, where $b_0 : \Lambda_n \to W_0$ is the structure map, we get a tautological base $T$ over $W$ with $r_T = r$.

The map $\rho$ is finite étale and $W_0$ is a completed local ring of $A^r$. So the map from the local ring of $A^r$ at $u$ of the closed point to $W$ is flat and sends the maximal ideal onto the maximal ideal, and the residue field extension is finite and formally unramified. The relation $\beta(c_0(e_i)) = \mathrm{pr}_i \circ u$ holds by the choice of $p_i$. So these data form a lower base $L$, with $h_L = h$.

It remains to compare $L$ with $v$. Since $\rho$ is finite étale and $V_1$ is a complete discrete valuation ring, there are a CN discrete valuation ring $V'$, an injective, finite, local map $f : V_1 \to V'$ and a local map $\kappa : W \to V'$ with $\kappa \circ \rho = f \circ \psi$. Then $\operatorname{Spec}\kappa$ followed by $u$ equals $\operatorname{Spec} f$ followed by $v$, and $\kappa \circ b = f \circ b_1$. Let $B'$ be the pullback of $A_v$ along $\operatorname{Spec} f$, with $\beta' : B' \to A_v$. By the pasting of pullback squares, there is a map $\beta'' : B' \to B$ that makes $B'$ the group pullback of $B$ along $\operatorname{Spec}\kappa$, and $\beta \circ \beta''$ equals the map $B' \to A_v \to A$. The two pullbacks of $P$ to $B' \times B'$ are then the same, and $\Lambda(M) \cong (\beta \times \beta)^* P$ gives the isomorphism of bundles. Take $e$ to be the identity. For $a \in \mathbb{Z}^r$, the section $c_v(n a)$ pulls back along $\operatorname{Spec} f$ to a section $x$ of $B'$. Pullback of sections is additive, and both $c_v$ and $c_0$ are sums of coordinate points, so $\beta''(x) = c_0(n a)$ over $\operatorname{Spec}\kappa$. $\square$

**Theorem 9.4.5 (Lower base for a trait).** Let $V$ be a CN domain that is a discrete valuation ring, let $b : \Lambda_n \to V$, let $(A_V, L_V)$ be a polarized abelian scheme over $V$ of relative dimension $g$, let $r \ge 0$, and let $c : \mathbb{Z}^r \to A_V(V)$ be additive. Then there are a lower base $L$ of level $n$ over $\Lambda_n$ with ring $W$, tautological base $T = (b_T, B, M, r_T, c_0, \tau_0)$ and $h_L = g$, a discrete valuation ring $V'$ that is a CN domain, an injective, finite, local map $f : V \to V'$, a local map $\kappa : W \to V'$ with $\kappa \circ b_T = f \circ b$, and an isomorphism $e : \mathbb{Z}^{r_T} \to \mathbb{Z}^r$ with the following properties. There are a group scheme $B'$ over $V'$ and maps $\beta' : B' \to A_V$ and $\beta'' : B' \to B$ that make $B'$ the group pullback of $A_V$ along $\operatorname{Spec} f$ and of $B$ along $\operatorname{Spec}\kappa$, such that
$$(\beta' \times \beta')^* \Lambda(L_V) \cong (\beta'' \times \beta'')^* \Lambda(M),$$
and for each $a \in \mathbb{Z}^{r_T}$ there is a section $x \in B'(V')$ with $\beta'(x) = c(e(a))$ over $\operatorname{Spec} f$ and $\beta''(x) = c_0(n a)$ over $\operatorname{Spec}\kappa$.

Lean: `GlobalTheory.TChart.exists_lowBase_of_trait` (also `GlobalTheory.T.exists_lower_base_of_trait_abelian_part`, a wrapper).

*Proof.* A lemma on polarized abelian schemes over traits gives a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$, a CN discrete valuation ring $V_1$ with an injective, finite, local map $f_1 : V \to V_1$, and a point $v : \operatorname{Spec} V_1 \to A^r$ over $f_1 \circ b$, with a group pullback $\beta_1 : A_v \to A_V$ along $\operatorname{Spec} f_1$ such that $P_v \cong (\beta_1 \times \beta_1)^* \Lambda(L_V)$ and $\beta_1(c_v(n a)) = c(a)$ over $\operatorname{Spec} f_1$ for each $a$. In words: after a finite extension, the polarized abelian scheme gets a level $n$ structure, and the points $c(a)$ get $n$-th roots in a way compatible with addition.

Apply the theorem on points of a fibre power to $F$, $r$, $V_1$, $f_1 \circ b$ and $v$. It gives $L$, $V'$, $f$, $\kappa$, $e$, $B'$, $\beta'$, $\beta''$ and the sections. We use $f \circ f_1 : V \to V'$, which is injective, finite and local, and $\beta_1 \circ \beta' : B' \to A_V$. A composite of group pullbacks is a group pullback, and a composite of squares is a square. The bundles compare by
$$(\beta_1\beta' \times \beta_1\beta')^* \Lambda(L_V) \cong (\beta' \times \beta')^* P_v \cong (\beta'' \times \beta'')^* \Lambda(M).$$
For $a \in \mathbb{Z}^{r_T}$ the section $x$ satisfies $\beta_1(\beta'(x)) = \beta_1(c_v(n\,e(a))) = c(e(a))$ over $\operatorname{Spec}(f \circ f_1)$, and $\beta''(x) = c_0(n a)$. $\square$

**Remark 9.4.6 (Formalization).** In the proof of the theorem on points of a fibre power, the isomorphism $e$ is the identity ([SiegelFibrePowerPointLiftsToLowerBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SiegelFibrePowerPointLiftsToLowerBase.lean#L195)), and $r_T = r$; the statement keeps $e$ only to fit the statement of the trait theorem, where it is also the identity. The name of the trait theorem speaks of "the abelian part of a trait", but its statement takes the polarized abelian scheme and the points directly, with no trait and no semi-abelian scheme ([ExistsLowerBaseOfTraitAbelianPart.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsLowerBaseOfTraitAbelianPart.lean#L17)). The lemma that gives the level structure and the $n$-th roots, the lemma that gives $V'$, and the lemma that gives the cubical periods $\tau_0$ have no entries in this chapter; the sentence "after a finite extension, the polarized abelian scheme gets a level $n$ structure" is our reading of the first one's statement. The condition on $u$ in a lower base is the Lean predicate of an étale completion together with formal unramifiedness of the residue map; we have not looked further into why both are kept.
