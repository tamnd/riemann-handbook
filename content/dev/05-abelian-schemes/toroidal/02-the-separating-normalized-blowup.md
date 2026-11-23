---
title: The separating normalized blowup
decls:
  - GlobalTheory.T.unitaryToroidalSeparation_of_base
  - GlobalTheory.UPoincTop.uStB
  - GlobalTheory.UPoincTop.uPoinStX_sep
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The separating normalized blowup

This section builds the candidate for the toroidal compactification. We start from a minimal compactification $Z$ of the moduli scheme over a Dedekind ring, we take a boundary ideal $J$ that vanishes along each boundary trait to the order given by the fan, and we take the normalized blowup $S \to Z_F$ of $J$ over the coefficient field. The theorem of this section says that $S$ has the properties the toroidal compactification needs, and that $S$ *separates*: two points of the boundary of $S$ with the same image carry degeneration data that are defined over the field of definition of that image. [The theorem on rigid charts from a separating blowup](/entry/rigid-boundary-charts-for-fan-of-unitary-separation/) uses this to prove the theorem on rigid charts for a fan in Section 1. We use the notation of Section 1.

**Definition 7.2.1 (Minimal compactification).** Let $X$ be a moduli scheme for $D$ and $l$, and $F$ a coefficient field. A *minimal compactification* $C$ of $X_F$ consists of:

1. a Dedekind domain $o$ of finite type over $\mathbb{Z}$ with an injective map $b : o \to F$ such that $F$ is the field of fractions of $b(o)$, in which $M'$, $d$ and the discriminant of $E$ are units;
2. a normal scheme $Z_C$, projective over $o$, and an open immersion $i_F : X_F \to Z_C \times_o F$ over $F$ whose image is dense, such that the composite $i : X_F \to Z_C$ also has dense image;
3. an ample line bundle $\mathcal{O}_Z(1)$ on $Z_C$ and an integer $N \ge 1$ such that, for each model $Y$ of $X_F$ over $\mathrm{id}_F$ and each map $f : Y \to Z_C \times_o F$ with $f \circ j = i_F$, if $\omega_Y$ is a line bundle then $f^* \mathcal{O}_Z(1) \cong \omega_Y^{\otimes N}$;
4. an *extension property*: let $R$ be a local domain that is a Mumford base, with a semi-abelian datum $t$ that has a uniformization, and let $y : \operatorname{Spec} \operatorname{Frac} R \to X_F$ be a point whose universal datum extends to $t$. Then each map $\operatorname{Spec} R \to \operatorname{Spec} o$ that is compatible with $y$ lifts to a map $\operatorname{Spec} R \to Z_C$ that extends $i \circ y$;
5. a condition of integrality on theta constants over normal schemes finite over $Z_C$.

Lean: `GlobalTheory.UPoinc.UCompact` (also `GlobalTheory.UPoinc.UCompact.i`).

This is the minimal (Satake-Baily-Borel) compactification of [toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications): a power of the Hodge bundle gives its projective embedding, and every degenerating family over a suitable local base has a limit in it. The existence of $C$ is [the theorem on integral minimal compactifications](/entry/unitary-integral-compactifications-exist/).

**Definition 7.2.2 (Order along boundary traits).** Let $j : X_F \to T$ be a map of schemes, $\varphi$ an invariant function, $J$ an ideal sheaf on $T$ and $d \ge 1$. We say that $J$ has *order $d\varphi$ along boundary traits* if the following holds. Let $W$ be a complete discrete valuation ring with uniformizer $\varpi$, $\chi : \operatorname{Spec} W \to T$ and $y : \operatorname{Spec} \operatorname{Frac} W \to X_F$ with $j \circ y = \chi|_{\operatorname{Frac} W}$. Let $t$ be a semi-abelian datum on $W$ that extends the universal datum at $y$, with a uniformization $P$ whose periods are monomial in $\varpi$ with exponent a level form $\beta$ of level $1$. Then there is $n \in \mathbb{N}$ with $n = d\,\varphi(\beta)$ and $\chi^* J = (\varpi^n)$.

Lean: `GlobalTheory.UPoinc.UValOn` (also `GlobalTheory.UPoinc.GenOf`).

So along a boundary trait with monodromy form $\beta$, the ideal $J$ vanishes to the order that $d \varphi$ gives to the ray of $\beta$. On a toroidal compactification the divisor of $d\varphi$ has this property, so $J$ is a candidate for the pushforward of that divisor.

**Definition 7.2.3 (Normalized blowup).** Let $\pi : S \to Z$ be a map of schemes and $J$ an ideal sheaf on $Z$. Then $\pi$ is a *normalized blowup* of $J$ if $S$ is normal and $\pi$ factors as $S \xrightarrow{\nu} S_0 \xrightarrow{\pi_0} Z$, where $\pi_0$ is the blowup of $J$, $\nu$ is finite, and $\nu$ is an isomorphism over a dense open $U \subseteq S_0$ with $\nu^{-1}(U)$ dense.

Lean: `GlobalTheory.Poinc.IsNormBl`.

**Definition 7.2.4 (Monomial family).** Let $V$ be a local domain. A *monomial family* over $V$ consists of a map $F \to V$, a semi-abelian datum $t$ on $\operatorname{Spec} V$ with a uniformization $P$ by degeneration data with character lattice $X_P$, a point $y : \operatorname{Spec} \operatorname{Frac} V \to X_F$ whose universal datum extends to $t$, elements $s_1, \dots, s_m$ of the maximal ideal, and forms $\delta_1, \dots, \delta_m$ on $X_P$, such that the $\delta_i$ form a cone of $\varphi$, $X_P$ has rank at most $\min(p, q)$, and the periods of $P$ are monomial in the $s_i$ with exponents $M' \delta_i$.

Lean: `GlobalTheory.UChart.MonoFam` (also `GlobalTheory.UChart.Fam`).

**Definition 7.2.5 (Separation at a point).** Let $V$ be a local domain with degeneration data $Q$, with abelian part $A$, line bundle $L$ and points $c(a) \in A$ for $a \in X_Q$. Let $s : \{1, \dots, m\} \sqcup \{1, \dots, N\} \to V$, let $\tau_0$ be generators for the period line bundles of $Q$, and let $\mathrm{ev} : V \to K$ be a ring map to a field with a subfield $k_0$. We say that $Q$ is *separated at $\mathrm{ev}$ over $k_0$* if:

1. $\mathrm{ev}(s(i)) = 0$ for the first $m$ indices;
2. there are an abelian scheme $B_0$ over $k_0$ with a line bundle $M_0$ and points $c_0(a)$, and an isomorphism of $\mathrm{ev}^*(A, L, c)$ with the base change of $(B_0, M_0, c_0)$ to $K$;
3. for each ring map $\iota : W_0 \to V$ such that $(Q, \tau_0)$ comes from a datum over $W_0$, if $\mathrm{ev}(\iota(W_0)) \subseteq k_0$ then $\mathrm{ev}(s(k)) \in k_0$ for the last $N$ indices.

Lean: `GlobalTheory.UChart.SepAtB` (also `GlobalTheory.UChart.FromBase`, `GlobalTheory.UChart.Gens`).

**Definition 7.2.6 (Separating map).** Let $j : X_F \to S$ be a map of schemes. Then $j$ is *separating* for $\varphi$ if the following holds. Let $V$ be a local domain that is a Mumford base, with a monomial family $(t, P, y, s, \delta)$ and a map $\xi : \operatorname{Spec} V \to S$ with $\xi|_{\operatorname{Frac} V} = j \circ y$. Extend $s$ by units $s(k)$, $k = 1, \dots, N$, and extend $\delta$ to a $\mathbb{Z}$-basis $\varepsilon$ of the balanced forms on $X_P$, such that the periods of $P$ are $\prod_k s(k)^{M' \varepsilon_k(a, b)}$ times the generators $\tau_0(a, b)$. Let $K$ be an algebraically closed field, $\mathrm{ev} : V \to K$ a ring map such that $\xi \circ \mathrm{ev}$ is constant at $\xi$ of the closed point, and $k_0 \subseteq K$ an algebraically closed subfield over which the point $\xi \circ \mathrm{ev}$ is defined. Then $P$ is separated at $\mathrm{ev}$ over $k_0$.

Lean: `GlobalTheory.UChart.SepB` (also `GlobalTheory.UChart.TauIn`, `GlobalTheory.Poinc.Sep.DefOver`).

Condition 1 of the separation says that the point lies on the closed stratum of the chart. Conditions 2 and 3 say that the abelian part and the remaining period coordinates are determined by the image point in $S$. So $S$ does not identify boundary points with different degeneration data.

**Definition 7.2.7 (Separating blowup data).** Let $X$ and $F$ be as above. *Separating blowup data* consist of a scheme $Z$ with a map $Z \to \operatorname{Spec} F$, a map $i : X_F \to Z$, a line bundle $\mathcal{O}_Z(1)$, integers $N, d$, an ideal sheaf $J$ on $Z$, a map $\pi : S \to Z$, a map $j : X_F \to S$ and an effective Cartier divisor $B$ on $S$ such that:

1. $Z$ is normal and projective over $F$, $i$ is an open immersion over $F$ with dense image, and $\mathcal{O}_Z(1)$ is ample;
2. $N \ge 1$, and $f^* \mathcal{O}_Z(1) \cong \omega_Y^{\otimes N}$ for each model $Y$ with a map $f : Y \to Z$ that extends $i$ and with $\omega_Y$ a line bundle;
3. the extension property of a minimal compactification holds for $Z$ over $F$;
4. $d \ge 1$, the support of $J$ does not meet $i(X_F)$, and $J$ has order $d\varphi$ along boundary traits through $i$;
5. $\pi$ is a normalized blowup of $J$, $S$ is projective over $F$, $j$ is an open immersion with dense image, $\pi \circ j = i$, $\pi^{-1}(i(X_F)) = j(X_F)$, the ideal of $B$ is $\pi^{-1} J \cdot \mathcal{O}_S$, and this ideal has order $d\varphi$ along boundary traits through $j$;
6. there is $k_0$ such that $\pi^* \mathcal{O}_Z(k) \otimes \mathcal{O}(-B)$ is ample for each $k \ge k_0$.

Lean: `GlobalTheory.UPoinc.UPoinOnX`.

**Theorem 7.2.8 (Separating normalized blowup).** Let $E$, $H$ and $D$ be as in Section 1 with $p + q \ge 1$, and let $\varphi$ be a polarized fan with no self-intersections in rank at most $\min(p, q)$. Then for each level $l$, moduli scheme $X$ and coefficient field $F$, there are separating blowup data $(Z, i, \mathcal{O}_Z(1), N, d, J, \pi : S \to Z, j, B)$ such that $j$ is separating for $\varphi$.

Lean: `GlobalTheory.UPoincTop.uPoinStX_sep` (also `GlobalTheory.UPoincTop.uStB` and `GlobalTheory.T.unitaryToroidalSeparation_of_base`, second names; `GlobalTheory.UChart.UStB`, the statement).

*Proof.* By [the theorem on integral minimal compactifications](/entry/unitary-integral-compactifications-exist/), there is a minimal compactification $C$ of $X_F$, with ring $o$, scheme $Z_C$ and map $i_F$. By [the theorem on the boundary ideal](/entry/u-ideal-st-holds/) of Section 4, there are $d \ge 1$ and an ideal sheaf $J_0$ on $Z_C$ whose support does not meet $i(X_F)$ and which has order $d\varphi$ along boundary traits through $i$.

Let $Z = Z_C \times_o F$ with the projections $f_Z : Z \to Z_C$ and $Z \to \operatorname{Spec} F$, and let $J = f_Z^{-1} J_0 \cdot \mathcal{O}_Z$. Since $F$ has characteristic zero and is the fraction field of $o$, the scheme $Z$ is normal and projective over $F$, and $f_Z^* \mathcal{O}_Z(1)$ is an ample line bundle. The support of $J$ is the preimage of the support of $J_0$, so it does not meet $i_F(X_F)$. Let $W$, $\chi$, $y$, $t$, $P$ and $\beta$ be as in the definition of the order along boundary traits for $J$ through $i_F$. Then $\chi' = f_Z \circ \chi$ is a trait of the same kind for $J_0$ through $i$, so $\chi'^* J_0 = (\varpi^n)$ with $n = d \varphi(\beta)$. Since $\chi^* J = \chi'^* J_0$, the ideal $J$ has order $d\varphi$ along boundary traits through $i_F$.

The open set $U = i_F(X_F)$ is dense in $Z$, and $J$ is the unit ideal on $U$. So there are a normalized blowup $\pi : S \to Z$ of $J$, with $S$ projective over $F$, and an effective Cartier divisor $B$ on $S$ whose ideal is $\pi^{-1} J \cdot \mathcal{O}_S$, such that $\pi$ is an isomorphism over $U$ and $\pi^{-1}(U)$ is dense in $S$. Let $j : X_F \to S$ be the composite of $i_F : X_F \cong U$ with the inverse of $\pi$ over $U$. Then $j$ is an open immersion, $\pi \circ j = i_F$ and $j(X_F) = \pi^{-1}(U)$, which is dense.

We take the line bundle $f_Z^* \mathcal{O}_Z(1)$ on $Z$ and the integer $N$ of $C$, and we check the six conditions. Condition 1 is the result on $Z$ above, together with the properties of $i_F$. For condition 2, let $f : Y \to Z$ extend $i_F$. Since $Z = Z_C \times_o F$, the third property of $C$ applies to $f$ and gives $(f_Z \circ f)^* \mathcal{O}_Z(1) \cong \omega_Y^{\otimes N}$, and this is $f^*$ of $f_Z^* \mathcal{O}_Z(1)$. For condition 3, let $R$, $t$, $y$ and $\sigma : \operatorname{Spec} R \to \operatorname{Spec} F$ be given. The extension property of $C$ for $\sigma$ followed by $\operatorname{Spec} b$ gives $\xi_0 : \operatorname{Spec} R \to Z_C$, and the pair $(\xi_0, \sigma)$ defines the map to $Z$. Condition 4 is the result on $J$ above. In condition 5, the order of $B$ along a trait $\chi$ through $j$ is the order of $J$ along $\pi \circ \chi$, which is a trait through $i_F$ because $\pi \circ j = i_F$. For condition 6, a result on blowups of noetherian schemes gives $k_0$ such that the pullback of $f_Z^*\mathcal{O}_Z(k)$ to $S$, twisted by $-B$, is ample for each $k \ge k_0$.

Finally, $j$ is separating for $\varphi$ by [the theorem on separation over the normalized blowup](/entry/sep-b-of-norm-bl/) of Section 6, applied to $C$, $d$, $J_0$, $\pi$ and $j$. $\square$

**Remark 7.2.9 (Formalization).** The proof is in [UnitaryToroidalSeparationOfBase.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryToroidalSeparationOfBase.lean#L23), and `uStB` at line 90 is the same term. The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The statements `UPoinOnX` and `UStB` are in [SpecializesGenericImage.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SpecializesGenericImage.lean#L153) and [FromBaseAlt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/FromBaseAlt.lean#L57). The three steps on $Z$, on the normalized blowup and on the ample twist use the lemmas `T.generic_fibre_normal_projective_ample_charZero`, `NormBlowupField.exists_normBl` and `BlowAmpleNoeth.ample_twist_of_blowup`. They have no entries in this chapter, and we use only their statements as the proof applies them. The term passes `IsProper π`, `IsOpenImmersion j` and $\pi^{-1}(i_F(X_F)) = j(X_F)$ to the theorem of Section 6, which does not use them. We have not unfolded `Mum.Base`, `CDvr`, `PELUnif`, `IsMonomial`, `DegPre`, `FromBase`, `IsGrpPullback`, the field `thetaInt` of `UCompact`, or `FinalTheorems.Blowup`. The description of `FromBase` in the separation above is a summary of its statement.
