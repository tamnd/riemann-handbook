---
title: The shape theorem
decls:
  - GlobalTheory.Top.closed_linkEta_of_duty
  - GlobalTheory.Top.designExists_of_tuSize_aux4n_litThin
  - GlobalTheory.Top.link_alt_alt_bis
  - UpperTheory.Top.shape_closed_link_n_of_green
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The shape theorem

This section proves the shape theorem. From the statement [Green](/step/green-def/) on cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_g)$, it gives a long implication whose conclusion is the connectedness statement $\mathrm{Top}_G$ of [ZeroFreeAll from $\mathrm{Top}_G$ and hosts](/entry/zero-free-all-of-top-g/). The step [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/) fills the hypotheses of the implication with the fields of [the record HypsAlt](/step/hyps-alt-def/). Three of the inputs are proved first: the bound $\mathrm{Link}_\eta$, the existence of designs, and the bound $\mathrm{Link}_S$.

We keep the notation of the last two sections: a family class $\mathcal{A}$, a twist selection on $\mathcal{A}$, the classes $\mathcal{A}'$ and $\mathcal{D}(\mathcal{A})$, and $\mathrm{Closed}(\mathcal{C}, P)$.

**Definition 3.6.1 (Duty and the bound $\mathrm{Link}_\eta$).** A family $F$ has *duty* if its data meet a list of conditions on the Galois data of its points. The bound $\mathrm{Link}_\eta(F)$ is a bound at the twisted places of $F$. A proved lemma gives it from three facts that hold eventually in $x$, for each $i$: a condition on the Galois data of $D(x,i)$, a Hecke condition on the same data, and a cover.

**Theorem 3.6.2 (The bound $\mathrm{Link}_\eta$).** Let $\mathcal{A}$ be a family class with a twist selection, and assume that each family of $\mathcal{A}$ has duty. Then $\mathrm{Closed}(\mathcal{D}(\mathcal{A}), \mathrm{Link}_\eta)$.

Lean: `GlobalTheory.Top.closed_linkEta_of_duty`

*Proof.* We show that $\mathrm{Link}_\eta(F)$ holds for every family $F$ of $\mathcal{D}(\mathcal{A})$; then it is closed. A lemma on tied families gives $x_0$ such that the selected choice at $F$ is tied at each $x \ge \max(x_0, x_1 + 1)$ and each $i$. The tie holds a Galois part with the two conditions, and a cover. These are the three facts, and the lemma gives $\mathrm{Link}_\eta(F)$. $\square$

**Definition 3.6.3 (Designs).** Let $c_T$ be a function of $\varepsilon$ and $C_{YL}$. *Design choices* on a class $\mathcal{C}$ with constant $3$ and $c_T$ are choices of designs for the families of $\mathcal{C}$. *Designs exist* in $\mathcal{C}$ with constant $3$ if for all small $\varepsilon$ the class has families at scale $\varepsilon$ with designs and large constants. The statement $\mathrm{MinkDiv}$ is a Minkowski bound on divisors. The statement $\mathrm{LitThin}$ is a thin set statement from the literature.

**Theorem 3.6.4 (Designs exist).** Let $\mathcal{A}$ be a family class, $c_T$ a function, and assume:

1. $\mathrm{MinkDiv}$ implies design choices on $\mathcal{A}'$ with constant $3$ and $c_T$;
2. a twist selection on $\mathcal{A}$, and each family of $\mathcal{A}$ has duty;
3. closed on $\mathcal{A}'$: if $c_T(\varepsilon, C_{YL}) \le C_{Tu}$, then $\mathrm{TuSize}(F)$;
4. closed on $\mathcal{A}'$: for all $x > x_1$ and all $i$, the class number formula in the second form holds for $D(x,i)$ and its level;
5. $\mathrm{LitThin}$.

Then designs exist in $\mathcal{A}'$ with constant $3$.

Lean: `GlobalTheory.Top.designExists_of_tuSize_aux4n_litThin`

*Proof.* The Minkowski bound is proved, so hypothesis 1 gives design choices. The design choices pass up from $\mathcal{A}'$ to the classes with more conditions. The duty gives that the linked families are aligned, and a lemma on linked closed rank ties gives the second layer of the family class. A chosen proviso holds with an exponent $e \le 3$. The thin condition of the chosen designs is closed, by $\mathrm{LitThin}$. With hypotheses 3 and 4, a lemma on design choices gives designs. $\square$

**Definition 3.6.5 (The bound $\mathrm{Link}_S$).** $\mathrm{Link}_S(F, 3)$ is the bound of the transport form of Theorem S at the family $F$ with constant $3$.

**Theorem 3.6.6 (The bound $\mathrm{Link}_S$).** Let $\mathcal{A}$ be a family class with a twist selection and a spectral condition on the selection. Assume:

1. the Wu decay of the gap, and finite dimension of the rows;
2. closed on $\mathcal{D}(\mathcal{A})$: the frame bound with the parameters $(C_{YL}+1, \tfrac14, 3, \tfrac12, C_{Tu}, 3)$;
3. counting constants $c_{30}$ for each list of reals, with $0 \le C$ and $2(C_{YL}+1) \le A$ for the constants of each family;
4. the type, row and main row statements of the positive rows;
5. the loop row statement and, closed on $\mathcal{D}(\mathcal{A})$, Theorem S at the selected data with constant $3$;
6. closed on $\mathcal{D}(\mathcal{A})$: the count of all points of the class with the constants $c_{30}$;
7. at each selected point, the volume is independent of the signature and the class items hold at the rank of the first space.

Then $\mathrm{Closed}(\mathcal{D}(\mathcal{A}), F \mapsto (\mathrm{TuSize}(F) \Rightarrow \mathrm{Link}_S(F, 3)))$.

Lean: `GlobalTheory.Top.link_alt_alt_bis`

*Proof.* This is [the transport of Theorem S](/entry/theorem-s-transport-link-zero/) applied to $C_0 = 3$ and the hypotheses. The residue condition that it also needs holds on every class, by a closed lemma with no hypotheses. $\square$

**Definition 3.6.7 (The bounds of the shape theorem).** For a class $\mathcal{C}$, the bound $\mathrm{Link}_N$ bounds a weighted sum over twisted places by the size parameters plus the sum of the Sha lengths $\sum_l \mathrm{vv}(l)$. The bound $\mathrm{Link}_{IRR}$ is a bound on irreducible labels, $\mathrm{Link}_{\mathrm{DIV}}$ the division kernel bound, and $\mathrm{Link}_{\mathrm{GLOBAL}}$ a global mass bound. The *shape implication* $\mathrm{Shape}(N)$ for a slot $N$ on classes is this statement: for each family class $\mathcal{A}$, the 52 hypotheses of the shape form on $\mathcal{A}$, with $N(\mathcal{D}(\mathcal{A}))$ among them, imply $\mathrm{Top}_G$. The hypotheses are a twist selection and its bundle of choices, the duty of each family, conditions on the rows of each selected datum, seventeen closed bounds, some uniform statements ($\mathrm{LitThin}$, the Wu decay, finite dimension of rows, and mass and genus statements for all data), and the slot.

**Theorem 3.6.8 (The shape theorem).** Assume Green. Then $\mathrm{Shape}(N)$ holds for the slot $N(\mathcal{C}) = \mathrm{Closed}(\mathcal{C}, \mathrm{Link}_N)$.

Lean: `UpperTheory.Top.shape_closed_link_n_of_green`

*Proof.* Fix $\lambda > 1$, a requirement $G$, hosts with $G.\mathrm{req}$ on windows of scale $\lambda$, and the bound $\mathrm{HypV}$ on $G.\mathrm{cls}(\lambda)$. A design lemma on windows takes the class $\mathcal{C}$ of $\mathcal{A}$ with the five extra conditions, the class $\mathcal{C}'$ of $\mathcal{A} \cap G.\mathrm{cls}(\lambda)$ with the same conditions, the class $\mathcal{E} = G.\mathrm{cls}(\lambda)$, and the constants $C_0 = 3$, $C_{\mathrm{abs}} = 2$, $e_D = 2$, $e_L = 0$. It asks that designs exist in $\mathcal{C}'$ and that nine bounds are closed on $\mathcal{D}(\mathcal{A})$. It then picks a family with large constants and gets the chain tie from the nine bounds, so $\mathcal{E}$ is connected. The inputs are these.

1. Designs: [designs exist](/entry/design-exists-of-tu-size-aux4n-lit-thin/), from the design choices at $(\lambda, G)$, the size bounds, the class number formula and $\mathrm{LitThin}$.
2. $\mathrm{Link}_N$: the slot $N(\mathcal{D}(\mathcal{A}))$.
3. $\mathrm{Link}_\eta$: [the bound $\mathrm{Link}_\eta$](/entry/closed-link-eta-of-duty/), from the duty.
4. $\mathrm{Link}_{IRR}$: a joint count lemma, from Green and a count bound. Green gives the admissible label weights of each datum through the parametrisation of the [[cuspidal|9AZ164C298]] characters. This is the only use of Green.
5. The rank equality at small levels: a lemma on the selection and the surjectivity slot.
6. $\mathrm{Link}_{\mathrm{DIV}}$: a bridge kernel lemma, applied to the division kernel bound. That bound joins [the remaining division bounds at the constant 2](/entry/link-brest-alt/), a cut lemma, a wiring lemma, [the valuation bound on the working class](/entry/closed-family-admissible-twist-link-alt/) and a selection lemma from the Wu decay.
7. The full $\nu$ condition with the rank condition, and $\mathrm{Link}_{\mathrm{GLOBAL}}$: from the tie and the mass and genus slots.
8. $\mathrm{Link}_G$: [the concrete $\mathrm{Link}_G$](/entry/link-g-concrete5/), through a closed lemma from the duty.
9. $\mathrm{Link}_S$: [the bound $\mathrm{Link}_S$](/entry/link-alt-alt-bis/).

The rest is inclusions between classes and joins of closed bounds. $\square$

**Remark 3.6.9 (Formalization).** The theorems are in [LinkEta.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkEta.lean#L13) (line 13), LinkEx.lean (line 15), LinkAltAltBis.lean (line 16) and TopShape.lean (line 33), all in the folder `ThirdPlaceSeries`.

- In `closed_linkEta_of_duty` the duty hypothesis is introduced as `_` at line 16 and never used. The bound $\mathrm{Link}_\eta$ holds on $\mathcal{D}(\mathcal{A})$ from the selection alone.
- `designExists_of_tuSize_aux4n_litThin` and `link_alt_alt_bis` both need `set_option maxHeartbeats 1600000` (LinkEx.lean line 14, LinkAltAltBis.lean line 15). Each proves a fact `hC0'` (LinkEx.lean line 26, LinkAltAltBis.lean line 36) that it never uses.
- The name `shape_closed_link_n_of_green` says "closed LinkN", but the theorem does not prove that $\mathrm{Link}_N$ is closed. It takes this as the slot `nRest` and passes it on. The content comes from HypsAlt in the caller.
- The slots `hVC` and `nR` of the shape form are never used; here both are `True`.
- We have not unfolded `Duty`, `LinkEta`, `LinkS`, `LinkIRR`, `LinkGLOBAL`, `LitThin`, `MinkDiv`, `ChainTied` or `HypV`, and we have not checked which of the 52 hypotheses carry content.
