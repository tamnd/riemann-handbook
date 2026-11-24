---
title: A class and a selection from a linked row
decls:
  - UpperTheory.Top.classSel
  - UpperTheory.Top.recS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A class and a selection from a linked row

This section proves step 3 of [the record from all rows](/entry/nonempty-hyps-of-all-rows-alt/) of the chapter on the unitary hypotheses. The joined linked row gives a property of bundles. From it we build one family class $\mathcal{A}$ and one selection $\sigma$. The class has the seven duties and stable members. Under the Minkowski divisor condition it has design families, so that the record of hypotheses can be filled. The design families come from records of existence through kits of points. We prove that part first.

### The setting

We keep the language of the chapter on the unitary hypotheses: slots $Q$, $Q'$ and $R$, a linkage $\Lambda$, a property $K$ of bases, the large base condition $\mathrm{LB}(K, Q, R)$, rows $\mathrm{Row}(Q, \Lambda, H)$ and linked rows

$$\mathrm{Lg}(K, Q, Q', S \mapsto \mathrm{Row}(S, \Lambda, H)).$$

We write $\mathrm{RowL}(K, Q, Q', \Lambda, H)$ for this linked row. The statement $\mathrm{ExBL}(K, Q, Q', \Lambda)$ says that there is a slot $R$ with $\mathrm{LB}(K, Q, R)$ such that, eventually, each point of $Q' \wedge R$ has a bundle for each $c$ that $\Lambda$ links.

A *parameter set* $\kappa$ consists of a scale exponent $\varepsilon$, a constant record $C$ and five reals $c_D$, $c_h$, $C_5$, $c_6$, $C_b$. It is *positive* if $C_5$, $c_6$ and $C_b$ are positive. A family $F$ is *linked* to $\kappa$ if $F$ has the exponent $\varepsilon$, $\kappa$ is positive, $C$ is standard, and the lists of constants of $F$ agree with those of $C$. At $x$ above its threshold and an index $i$, a family has a datum $D_{x, i}$ and an object $O_{x, i}$ over it.

Let $\mathrm{QO}$ assign to each parameter set $\kappa$ a property $\mathrm{QO}_\kappa$ of pairs of a datum and an object. Let $\mathrm{QD}(D, O)$ say three things: each tuple of $D$ is used, the twists at $O$ are good at all places, and the member lattices of $D$ are stable under the ring of integers of the row field. The *class* of $\mathrm{QO}$ is

$$\mathrm{cl}(\mathrm{QO}) = \{F : F \text{ is linked to some } \kappa \text{ and } F \text{ is in the point class of } \mathrm{QO}_\kappa \wedge \mathrm{QD}\}.$$

A family of the point class has, eventually, the property at each of its objects, together with the page conditions, the wall condition and the twist conditions. So each family of $\mathrm{cl}(\mathrm{QO})$ has the seven duties and stable members.

The *existence statement* $\mathrm{ExD}(\mathcal{A}, c_T)$ for a class $\mathcal{A}$ and a cutoff $c_T$ says: for every $\lambda > 1$ and every requirement $G$ on hosts, if hosts with $G$ exist along scales of ratio $\lambda$, then there are design choices with the constant $3$ and the cutoff $c_T$ for the class of the families of $\mathcal{A}$ with good twists that meet $G$ at $\lambda$. Design choices give, for each small $\varepsilon$ and each transported constant, a family of the class that is large, has the chosen data, the boxes, the tame distinctness and the bound $c_T(\varepsilon, C_{\mathrm{YL}}) \leq C_{\mathrm{Tu}}$.

The *record of existence* for $\mathrm{QO}$ says that, for parameter sets that are eventually large in the usual order of the constants, there are $c_s > 0$ and $x_0$ with the following property. At each scale $s$ with exponent $\varepsilon$ and $x_0 \leq s.x$, and for each good choice of a word datum $P$, there are dimensions and a discriminant with the logarithmic bound $c_s\, m\, L \leq \log(\cdots)$. For each level choice with these values there is a datum $D$ with a layer over $P$, with the record and ledger conditions, such that each ledger point $p$ at $s$ with the weights and values has the property $\mathrm{QO}_\kappa$ at its datum and object.

### Design families from records

**Theorem 7.22.1 (Design families from records).** Assume the Minkowski divisor condition. Let $\mathrm{QO}$ be a property of objects depending on parameter sets and $c_T$ a cutoff. Assume that, under the Minkowski divisor condition, the record of existence holds for $\kappa \mapsto \mathrm{QO}_\kappa \wedge \mathrm{QD}$. Then $\mathrm{ExD}(\mathrm{cl}(\mathrm{QO}), c_T)$ holds.

Lean: `UpperTheory.Top.recS`.

*Proof.* Fix $\lambda > 1$ and a requirement $G$ with hosts along scales of ratio $\lambda$. We take the steps in order.

1. The relation for primes in progressions gives a small prime of residue $1$: there is $A \geq 1$ such that for each $M \geq 2$ there is a prime $p \equiv 1 \pmod M$ with $p \leq M^A$.
2. The norm primes and the level prime are given by a theorem without hypotheses. With the record of existence, the theorem on objects of an admissible twist datum gives object choices: eventually in the parameters and above a threshold, each good host at each scale has a point with the property $\mathrm{QO}_\kappa \wedge \mathrm{QD}$ at its object, with the host arithmetic and the canonical instance.
3. By step 1, hosts with $G$ give hosts with $G$ and the small prime condition. Forget the property of the points of step 2: they give object choices for the true property. The window share requirement in closed form is a theorem. These three facts give hosts with windows along scales of ratio $\lambda$.
4. The hosts with windows and the object choices of step 2 give kits: at each scale of the sequence a kit of points, each with the duties, the property $\mathrm{QO}_\kappa \wedge \mathrm{QD}$, the wall condition and $G$, with the thick set bound, the bad character bound and the quadratic divisor bound.
5. The design theorem turns the kits into design choices with the constant $3$ and the cutoff $c_T$, for the class of the families that are linked to some $\kappa$, lie in the point class of $\mathrm{QO}_\kappa \wedge \mathrm{QD}$, meet $G$ at $\lambda$ and have good twists. This class is the class of the existence statement for $\mathrm{cl}(\mathrm{QO})$.

This proves the theorem. $\square$

The Minkowski divisor condition is used twice: in the record of existence and in the design theorem.

### The class and the selection

For a slot $S$, a linkage $\Lambda$ and a property $E$ of bundles that may depend on $\kappa$, a bundle $b$ at $(D, O)$ and $c$ is *built* at $\kappa$ if it comes from a context of $\kappa$ and a point of $S$ with datum $D$ and object $O$, and $\Lambda$ links it at $c$. Put

$$\mathrm{QO}^{E}_\kappa(D, O) \iff \bigl(\kappa \text{ positive} \Rightarrow \forall c\ \exists b \text{ at } (D, O, c) \text{ built at } \kappa \text{ with } E_\kappa(b)\bigr).$$

The class of $E$ is $\mathrm{cl}(\mathrm{QO}^E)$. For a family of this class, at each $x$ and $i$ there is a built bundle with $E$ at $(D_{x, i}, O_{x, i})$ and the size constant of $F$. The *pick* $\pi_E$ chooses one. A selection $\sigma$ for a class $\mathcal{A}$ *is a selection at* $S$ with property $E'$ if each family of $\mathcal{A}$ is linked to some $\kappa$, lies in the point class of the true property, and each selected bundle is built at $\kappa$ from a point of $S$ and has $E'$.

**Theorem 7.22.2 (A class and a selection).** Assume the Siegel mass ratio for CM data, and that at each datum the volume tie implies the volume ratio. Let $K$ be a property of bases, $Q$ and $Q'$ slots, $\Lambda$ a linkage, $H(\mathcal{A}, \sigma)$ a statement and $c_T$ a cutoff. Assume:

1. the Minkowski divisor condition implies the base condition, the first and the second retwisting condition and the export condition for $K$, $Q$ and $Q'$;
2. $\mathrm{ExBL}(K, Q, Q', \Lambda)$ holds;
3. $\mathrm{RowL}(K, Q, Q', \Lambda, H)$ holds.

Then there are a family class $\mathcal{A}$ and a selection $\sigma$ for $\mathcal{A}$ with these properties:

1. the Minkowski divisor condition implies $\mathrm{ExD}(\mathcal{A}, c_T)$;
2. each family of $\mathcal{A}$ has the seven duties and stable members;
3. $\sigma$ is a selection at $Q'$ with the true property;
4. $H(\mathcal{A}, \sigma)$ holds.

Lean: `UpperTheory.Top.classSel`.

*Proof.* We take the steps in order.

1. The linked existence and the linked row may use different slots. Their conjunction $R$ has $\mathrm{LB}(K, Q, R)$, bundles at the points of $Q' \wedge R$, and the row $\mathrm{Row}(Q' \wedge R, \Lambda, H)$, since a row holds at each smaller slot.
2. The row gives a property $E$ of bundles such that, eventually, each bundle at a point of $Q' \wedge R$ that $\Lambda$ links has $E$, and $H$ holds at every selection of bundles with $E$. With the bundles of step 1 we get, eventually, $\mathrm{QO}^E_\kappa$ at the datum and object of each point of $Q' \wedge R$. Put $\mathcal{A} = \mathrm{cl}(\mathrm{QO}^E)$ and $\sigma = \pi_E$, for the slot $Q' \wedge R$. The pick is a selection at $Q' \wedge R$ with property $E$, so $H(\mathcal{A}, \sigma)$ holds. This is property 4.
3. A selection at $Q' \wedge R$ is a selection at $Q'$, and $E$ implies the true property. This is property 3.
4. Each family of $\mathcal{A}$ lies in the class of a property of objects, so it has the seven duties and stable members. This is property 2.
5. For property 1, assume the Minkowski divisor condition. By the theorem on design families from records it suffices to give the record of existence for $\mathrm{QO}^E \wedge \mathrm{QD}$. Hypothesis 1 gives the four group conditions. Since $\mathrm{LB}(K, Q, R)$ holds eventually, the second retwisting condition for $Q$ and $Q'$ gives the one for $Q$ and $Q' \wedge R$.
6. The theorem on the final context parameters, with the Siegel mass ratio, the volume ratios, the four group conditions of step 5 and the eventual statement of step 2, gives the record of existence for

$$\kappa \mapsto \bigl(\kappa \text{ positive} \Rightarrow \mathrm{QO}^E_\kappa\bigr) \wedge \mathrm{QD}.$$

Since $\mathrm{QO}^E_\kappa$ already starts with the assumption that $\kappa$ is positive, this property is $\mathrm{QO}^E_\kappa \wedge \mathrm{QD}$.

This proves the theorem. $\square$

The class is the class of the families whose objects carry built bundles with $E$. So the selection is not a free choice: any choice of built bundles with $E$ works, and the pick takes one by choice. The record from all rows then keeps $\mathcal{A}$ and $\sigma$ for all its fields, since $H$ is the conjunction of all its rows.

**Remark 7.22.3 (Formalization).** The theorem `classSel` is at line 14 of [ClassSel.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ClassSel.lean#L14), and `recS` is at line 30 of [ObjCTrue.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/ObjCTrue.lean#L30). Step 1 of the class proof is `RowL.elim` and step 2 is `Row.elim` with `pick_isSel`; the class is `cls (sAnd Q' R) Lk E` and the selection is `pick`, a `Classical.choose`, in [ValidForConstructedPointClassesEventuallyWorking.lean](lean:Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ValidForConstructedPointClassesEventuallyWorking.lean#L254), where `QOf` is at line 254, `IsSel` at line 264 and the record of existence `RecExP` at line 190. The existence statement `ExD` is at line 38 of [Supply.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/Supply.lean#L38). Step 6 is `memberTop_final_contextParameters`, and the identification of the two properties is the local equation `e`, by `propext`. The property 3 that `classSel` proves is a weakening of the fact `hs` by `IsSel.mono`, and its caller drops it. In `recS` the hypothesis `hR` takes the Minkowski condition as an argument although `hM` is also a hypothesis. The helper `objC_true` at line 16 of the same file forgets the property of the points and keeps `trivial` in its place. Step 3 of `recS` uses `hostWW` and `hostQ` from [HostWW.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/HostWW.lean#L27) and [SmallestPrimePolynomialBound.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/SmallestPrimePolynomialBound.lean#L64), and steps 4 and 5 are `kitS` and `designS`. We did not unfold the design theorem, the record and ledger conditions or the theorem on the final context parameters.
