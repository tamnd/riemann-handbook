---
title: The core and the membership statement
decls:
  - GlobalTheory.Mem.Top.Bl.CoreAsm.stepW_core
  - GlobalTheory.T.exists_constructedCore_of_all_construction_stages
  - GlobalTheory.Mem.Top.Bl.KPxCond.baseCond_KPx
  - GlobalTheory.Mem.Top.Bl.PinW.step_pinned
  - GlobalTheory.Mem.Top.Bl.MemberEx2.step_start
  - GlobalTheory.Mem.Top.Bl.memberE_of_steps2
  - GlobalTheory.T.exists_member_of_construction_steps_secondPass
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The core and the membership statement

First we build a core from a pinned column datum at level four. The core uses the kernel data, the gauge and the column layer conditions of the earlier sections. Then we prove the base condition and the first steps of the construction, from an untwisted base to a pinned column datum. Last, we put these steps into the membership statement for a slot, which has a first pass and a second pass. The result is the input to [the membership statement from the construction steps](/entry/member-e-closing-alt-alt/).

### Steps

A context $K$ fixes the scales and the constants of the construction. A property holds eventually in the context if it holds for all contexts whose small parameter $\varepsilon$ is small enough and whose other parameters are large enough. A property holds at large bases if it holds for all bases $B$ over the context, with a frame $f$ and twist data $T$, that avoid some finite sets of primes and whose coefficient field contains some finite sets of algebraic numbers.

**Definition 1.8.1 (Forced primes and the base property).** The twist data $T$ contain the forced primes for $K$ and $B$ if every prime $p$ that is an auxiliary prime $g_i$, or the discriminant $d$ of the host, or at most the bound $X''(n)$ of the scale, is in the prime set of $T$. The base property $\mathrm{KPx}$ of $B$ and $f$ says that there are field data for which $B$ is exact with frame $f$, and that the prestage of $B$ is prepinned. A prestage is prepinned if the inclusion of the space $X'$ into the top space $X_m$ sends each frame vector of $X'$ to the frame vector of $X_m$ with the same index.

**Definition 1.8.2 (Steps).** Let $p$ and $q$ be properties of contexts, bases, frames and twist data. A step from $p$ to $q$ says: eventually in the context, for all large bases with frame $f$ and twist data $T$ such that $\mathrm{KPx}$ holds and $T$ contains the forced primes, $p$ implies $q$. For properties $p$ and $q$ of column data $w$, a column step from $p$ to $q$ is a step from the true property to the property that each $w$ with $p$ has $q$.

**Definition 1.8.3 (Base condition).** The base condition for $\mathrm{KPx}$ says that, eventually in the context, there are bases over the context with $\mathrm{KPx}$ that can be enlarged by any finite sets of data, and that $\mathrm{KPx}$ passes from a base to each of its enlargements.

A slot $\mathcal{S}$ is a set of four position properties for the stages of the construction. For a slot, a column datum $w$ has level three or level four if the construction from $w$ reaches that level with the positions of $\mathcal{S}$. A core of $w$ at a later stage $Z$ is built from $\mathcal{S}$ if there is a certificate that ties the core to the level four object of $w$ and to $\mathcal{S}$. It is built with explicit entries if, in addition, the entry datum of its kernel certificate is the datum that place matrices and the kernel entry conditions give.

### The core

**Theorem 1.8.4 (Construction of the core).** Let $\mathcal{S}$ be a slot. Assume that each level four object of $\mathcal{S}$ has ambient data, a divisor datum and a theta datum, in the sense of the three existence conditions of the slot. Then there is a column step from "pinned and of level four for $\mathcal{S}$" to "has a core built from $\mathcal{S}$ with explicit entries".

Lean: `GlobalTheory.Mem.Top.Bl.CoreAsm.stepW_core` (also `GlobalTheory.T.exists_constructedCore_of_all_construction_stages`, a second name)

*Proof.* Step 1 (Gathering). The pinned property is a column step from the hypothesis. We combine it with the three existence conditions and the theorem on a lattice instance and a kernel certificate. So eventually in the context, at all large bases, each pinned column datum $w$ with a level four object $l$ at a later stage $Z$ has the following data.

1. Ambient data $a$ and $a_0$ with their properties.
2. A divisor datum $Y$ with its certificate, with the condition on the multiplicities $M_j$, with $\kappa_R(\sigma) = \kappa^\sharp$ for each $\sigma$, and with a position object for each object over $Y$.
3. A theta datum with its certificate.
4. A lattice instance $G_y$, a kernel family, the lattice layer conditions, a kernel certificate, place matrices and a proof of the kernel entry conditions whose entry datum is the entry datum of the certificate.

For item 4 we use the column data at split primes of $l$, the set $W_t$ of $l$, its tied choice, and the primes of $Y$.

Step 2 (Gauge). The host of the stage datum is a CM extension $E/F$. By the existence of a gauge, there is a gauge $G$ for $E/F$.

Step 3 (Object). The object of the core collects the gate ties and the comparison of the column data, the theta datum, the twisted forms, the lattice instance $G_y$, the error data of the hermitian columns, the tied choice and the export data of $l$, the level of the hermitian columns, the divisor datum $Y$, the base point of $l$, the kernel family, the ambient data and the gauge $G$. By item 2 of step 1, there is a position object for this object.

Step 4 (Forced values). Let $L$ be a size datum at the scale of $K$, let $v$ be a place that is not in $W_t$, and let $j$ be a lift index. The forced value of $L$ at $j$ and $v$ is the scale of the forced content at the residue characteristic of $v$. The level four object defines $W_t$ as the set of places at which some forced content is not zero. So the forced value is $0$.

Step 5 (Row layer). The row layer conditions for $Y$ follow from the row data of $l$. The only part that needs an argument is the condition at untwisted places. Let $v$ be a place where the character $\mu_v$ is the reference tuple. If $v$ were in $W_t$, then the character of $v$ would be both the twisted value of $l$ and the trivial character of the reference tuple. The twist data do not allow this, so $v \notin W_t$, and the untwisted condition of $l$ applies.

Step 6 (The core). The core has the following fields: the context and the character $\xi$ of $w$, the set $W_t$, the character $\mu$, the forced primes, the forced values of step 4, the object of step 3, the column layer conditions at later stages for the column data of $l$, the gate numbers of $l$, the lattice layer conditions of step 1, the row layer of step 5, the stability of the multiplicity data, the theta certificate, the fact that $G$ is a gauge, and the real, volume and character data of $l$.

Step 7 (Certificate). The certificate that the core is built from $\mathcal{S}$ takes its fields from the pin, from $l$, from the kernel certificate of step 1, from the divisor and theta certificates, from the ambient data and from the position object. The kernel entries of step 1 show that the core is built with explicit entries. $\square$

The gauge of the core is the gauge $G$ of step 2. It enters the core in two places: as a field of the object, and through the condition that it is a gauge.

### The base condition and the first steps

The four following statements are hypotheses from the literature, in the form that the formal proof uses. Their sources are listed in the notes of this chapter.

1. (Ray class fields) For each number field $k$ and each nonzero modulus $\mathfrak{q}$, there is an abelian extension of $k$ that is unramified outside $\mathfrak{q}$, whose Galois group is generated by the Frobenius elements, and in which an ideal prime to $\mathfrak{q}$ is trivial for all characters if and only if it has a generator of the correct ray class.
2. (Principal ideals) For a totally complex field $k$ and its ray class field $L$ of modulus $1$, which is the Hilbert class field, each ideal of $k$ becomes principal in $L$.
3. (CM curves) For each prime $p > 3$ with $p \equiv 3 \pmod 4$, there is an elliptic curve over the field $\mathbb{Q}(j)$ of its $j$-invariant, whose period lattice is the ring of integers of $\mathbb{Q}(\sqrt{-p})$, that has good reduction outside $p$ and minimal discriminant $-p^3$.
4. (Siegel mass ratio) For each CM field $k$ that satisfies the unramified condition of the mass formula and each $M \ge 3$, the ratio of the masses of the standard hermitian lattices of ranks $M$ and $M-1$ is the explicit right side of the mass formula.

**Theorem 1.8.5 (The base condition).** Assume (1) to (4). Then the base condition holds for $\mathrm{KPx}$.

Lean: `GlobalTheory.Mem.Top.Bl.KPxCond.baseCond_KPx`

*Proof.* By (1), (2) and (3), the exactness part of $\mathrm{KPx}$ satisfies the base condition in the form of the field data. It is then sufficient to give, eventually in the context, a prestage over the context that is prepinned and has a frame. By (4), eventually in the context each prestage over the context has an extension and a frame. The coordinate prestage of the context is over the context, because its spaces are the diagonal spaces. It is prepinned, because the frame vectors of the coordinate spaces extend to bases in the same order. So the coordinate prestage, with its frame, has both properties. $\square$

**Theorem 1.8.6 (Pinned column data).** Assume (4). Then there is a step from the true property to the existence of a pinned column datum.

Lean: `GlobalTheory.Mem.Top.Bl.PinW.step_pinned`

*Proof.* Step 1 (Three eventual facts). By (4), eventually in the context, each prestage over the context has an extension and a frame. Eventually, large bases have the data of the canonical twist index. Eventually, large bases have column inputs with the required properties, and for these inputs the following two facts hold.

1. The values $\xi_a(P)$ of each character $\xi_a$ at the unramified primes $P$ lie in the coefficient field $L$. This is the fact that the inputs read the characters.
2. For each prime $P$ in the set $Q_a$, the field $L$ contains a primitive root of unity of order $|\mathcal{O}_E / P|$. To see this, note that $\xi_a$ is a twist, so there is a ramified prime $P'$ with the same norm. The finiteness of the twist set gives a root of unity of that order in $L$.

Step 2 (Selection). Fix a large base with $\mathrm{KPx}$ and the forced primes. There is a half selection of split places of the base, with places above each place of $F$. With this selection, the column inputs give an extension $X$ and inputs $I$ that are in good order, have their pins, are twisted, have their jets in the field, use the selection, have the frame $f$, the off set $S$ and the twist set of $T$ as range of $\xi$.

Step 3 (The pin). These data form a column datum $w$, with the laws and the base law that the good order of $I$ gives. The pin of $w$ records that $I$ is twisted, that its jets are in the field, that the fields satisfy the laws, the selection facts, the places over a common prime, and the two facts of step 1. $\square$

A column datum $w$ is a start if it is pinned, it has the support property, and the twist data are coherent.

**Corollary 1.8.7 (Start of the construction).** Assume (4). Then there is a step from "the twist data are untwisted" to the existence of a column datum that is a start.

Lean: `GlobalTheory.Mem.Top.Bl.MemberEx2.step_start`

*Proof.* By the theorem, there is a pinned column datum $w$. When the twist data are untwisted, $w$ has the support property and the twist data are coherent. $\square$

### The membership statement

For a slot $\mathcal{S}$, the membership statement has four parts: the base condition for $\mathrm{KPx}$; the first pass, which is a step from untwisted twist data to a core built from $\mathcal{S}$ with explicit entries; the export condition for these cores; and the second pass, which says that each such core that exports has an enlarged base at which there is a core that is built, satisfies the twist condition, and is good for $\mathcal{S}$.

**Theorem 1.8.8 (Membership from the construction steps).** Assume (1) to (4). Let $\mathcal{S}$ and $\mathcal{S}'$ be slots. Assume the following.

1. There are column steps from a start to level three for $\mathcal{S}$, and from pinned and level three to level four for $\mathcal{S}$.
2. The three existence conditions hold for $\mathcal{S}$.
3. The cores built from $\mathcal{S}$ with explicit entries export.
4. Each such core that exports has, at an enlarged base, a column datum that is a start and has level three for $\mathcal{S}'$.
5. There is a column step from pinned and level three to level four for $\mathcal{S}'$, and the three existence conditions hold for $\mathcal{S}'$.
6. Each core built from $\mathcal{S}'$ with explicit entries is good for $\mathcal{S}$, and its object satisfies the twist condition.

Then the membership statement holds for $\mathcal{S}$.

Lean: `GlobalTheory.Mem.Top.Bl.memberE_of_steps2` (also `GlobalTheory.T.exists_member_of_construction_steps_secondPass`, a second name)

*Proof.* Step 1 (Base). The base condition is the theorem above.

Step 2 (First pass). Start from untwisted twist data. The corollary on the start gives a column datum $w$ that is a start. Hypothesis 1 takes $w$ to level three and then to level four, and $w$ is still pinned. The construction of the core, with hypothesis 2, gives a core built from $\mathcal{S}$ with explicit entries. A column step to a core gives a step to the existence of a core, so this is the first pass.

Step 3 (Export). This is hypothesis 3.

Step 4 (Second pass). Start from a column datum that is a start and has level three for $\mathcal{S}'$. In the same way as in step 2, hypothesis 5 and the construction of the core give a core built from $\mathcal{S}'$ with explicit entries. By hypothesis 6 it is good for $\mathcal{S}$ and satisfies the twist condition. This gives a step to the existence of such a core. We compose hypothesis 4 with this step. The position of the new core then gives the three properties that the second pass needs: built for $\mathcal{S}$, the twist condition, and good for $\mathcal{S}$. $\square$

**Remark 1.8.9 (Formalization).** The theorem `stepW_core` takes the Siegel mass ratio hypothesis as `_h2b` and does not use it ([ExistsConstructedCoreOfAllConstructionStages.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsConstructedCoreOfAllConstructionStages.lean#L67)). The base condition is in [ExistsPrePin.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsPrePin.lean#L30), and the coordinate prestage is `exists_prePin` at line 26. The two facts of step 1 of the pinned theorem are the lemma `valsRoots` ([StepPinned.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/StepPinned.lean#L17)). The chain from a start to a built core is `stepW_builtE` ([ExistsMemberOfConstructionStepsSecondPass.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsMemberOfConstructionStepsSecondPass.lean#L28)). The four literature hypotheses are Lean propositions `RayField`, `PrincipalIdealSt`, `CMCurveGoodOutsidePrimeSt` and `SiegelMassRatioCM`.
