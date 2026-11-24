---
title: True volume stages and local families
decls:
  - GlobalTheory.PlaceOrbit.exists_locId
  - GlobalTheory.Mem.Top.Bl.TrueLocal.exists_isLocalFamily
  - GlobalTheory.Mem.Top.Bl.TrueLocal.isRecG_of_isLocalFamily
  - GlobalTheory.Mem.Top.Bl.TrueLocal.nonempty_columnLocalData_of_standardConcreteFamily
  - GlobalTheory.Mem.Top.Bl.TrueLocal.exists_trueVolume_stage_of_any_column_choice
  - GlobalTheory.Mem.Top.Bl.TrueLocal.exists_trueVolumeStage_columnChoiceStep
status: drafted
drafted_by: writer@claude-opus-5-5
---
## True volume stages and local families

A stage of the construction carries a volume for each Hermitian space and a local group datum, a gate, for each word $u$ and each place $w$. In this section we choose a stage whose volumes are the true volumes of the unitary quotients and whose gates come from local identifications of the completions. The local identifications are the first result. They give a local family, and a local family gives the column data at the split primes. The final theorem enters [the large unramified exponents](/entry/member-bundles-large-unramified-exponents-alt/).

### Local identifications

Let $E/F$ be the CM extension of the host and $p$ a prime that splits in $E$. Let $L$ be the coefficient field and $L_0$ a level datum. We use [places and completions](/learn/number-fields/#places-and-completions) and [the splitting of primes](/learn/number-fields/#the-splitting-of-primes).

**Definition 1.14.1 (Local identification).** A local identification at $p$ consists of:

1. a bijection between $\{0, \dots, n_V - 1\}$ and the places of $F$ over $p$;
2. for each such place $v$, an isomorphism of $\mathbb{Q}_q$ with the completion $F_v$, for $q = p^n$ with $n$ the order of Frobenius, that maps the integers $W$ of $\mathbb{Q}_q$ onto the integers of $F_v$;
3. for each such $v$, a splitting $E \otimes_F F_v \cong F_v \times F_v$ that sends $1 \otimes a$ to $(a, a)$ and that swaps the two factors under the conjugation of $E$;
4. frames $\mathrm{fr}_v \in \mathrm{GL}_k(F_v)$ that describe the local lattice.

Its embedding at $v$ is the first factor of the splitting followed by the inverse of the isomorphism of 2. So a local identification writes each completion of $E$ at $p$ as a pair of copies of an unramified extension of $\mathbb{Q}_p$, with fixed coordinates.

**Theorem 1.14.2 (Existence of local identifications).** Let $D$ be an ambient datum, $u$ a word, and $w$ a place of $L$ whose residue characteristic $p$ has a gate index. Then there are a local identification at $p$, a ring map $i_K$ from the completion of the record field at $w$ to $\mathbb{C}_p$, and a ring map $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$, such that $i_K$ restricted to $L$ is $\lambda$ composed with the embedding of $L$, and the positions of the local identification are correct for $i_K$, $\lambda$ and every character $\psi$.

Lean: `GlobalTheory.PlaceOrbit.exists_locId`.

*Proof.* Choose a good place $Q_0$ of $F$ over $p$ and an embedding $i_0$ of its completion into $\mathbb{Q}_{p^n}$, where $n$ is the order of Frobenius at $p$. The places of $F$ over $p$ are indexed by the orbit representatives of the Galois group of $\mathbb{Q}_{p^n}/\mathbb{Q}_p$ on the embeddings: the map from representatives to places is injective and surjective. The embedding $i_0$ gives an isomorphism at each place. Since $p$ splits in $E$, each place has a splitting with the two properties of 3. To match the given map $\lambda$, twist $i_0$ by a Galois automorphism $\gamma$ of $\mathbb{C}_p$, which exists because two embeddings of a number field into $\mathbb{C}_p$ differ by such an automorphism. The norm of the embedding gives the frames and the positions. $\square$

### Local families

**Definition 1.14.3 (Local family).** A family $g$ of gates is a local family for the forms $T$ and the level datum $L_0$ if there are local identifications $I_{u,w}$ at each gate, characters $\psi_{u,w}$ of the group away from 2 with values in the units of the record ring, a basis $B \in \mathrm{GL}_k(E)$ that is standard, and maps $i_K$ and $\lambda$, such that: the frames of $I_{u,w}$ are the base change of $B$ along the first factor of the splitting; $i_K$ on $L$ is $\lambda$ on the embedding of $L$; the positions are correct; each $\psi_{u,w}$ is tied to the level of the forms $T_u$; and $g$ is the gate built from $I$ and $\psi$.

**Proposition 1.14.4 (Existence of a local family).** Assume that $D$ is standard tied, that $L_0$ has a companion, that $L_0$ and $T_u$ are jointly of level zero, and that the character of level zero of $T_u$ is rational, for each $u$. Then there is a local family $g$ whose gates have the dimension of the space $M_{u,0}$ of level zero.

Lean: `GlobalTheory.Mem.Top.Bl.TrueLocal.exists_isLocalFamily`.

*Proof.* The theorem on local identifications gives $I_{u,w}$, with the standard basis of $D$ for the frames. A character $\psi_{u,w}$ away from 2 tied to the level exists by the rational character of level zero and the joint condition. Define $g$ as the gate of $I$ and $\psi$. Its dimension is the dimension of $M_{u,0}$ by construction. $\square$

**Theorem 1.14.5 (Recursion of a local family).** Under the hypotheses on joint level zero and rational characters, let $g$ be a local family of the dimension of $M_{u,0}$. Then the stage with gates $g$ carries gate ties, a lattice comparison and group compatibility data which satisfy the recursion condition, whose Hermitian levels of level zero are $L_0$, whose forms are the forms of level zero of $T$, and such that an integer $x$ of $F$ lies in the place of the Hermitian datum at a position if and only if the valuation at $w$ of the image of $x$ at that position is positive.

Lean: `GlobalTheory.Mem.Top.Bl.TrueLocal.isRecG_of_isLocalFamily`.

*Proof.* The comparison statements for the local identifications give the gate ties and the lattice comparison. The group compatibility of the recursion gives the compatibility data with the recursion condition, for the levels $L_0$ and the forms of level zero. The positions of the local identification are correct, so the place at a position is the prime of the integers where the valuation at $w$ is positive. A retie of the recursion moves the result from the gates of $I$ to the gates $g$. $\square$

**Corollary 1.14.6 (Column data at the split primes).** Let $w$ be a column datum, $Z$ a later stage and $C$ tied symmetric columns at $Z$ that are standard and standard in level. Let $g$ be a local family for the levels of $C$ and the forms of $C$. Assume that the stage $Z$ with gates $g$ has compatible volumes and that it is compatible with the constant $\omega$ for the constant $\delta$ of $w$. Then the column data at the split primes exist at this stage.

Lean: `GlobalTheory.Mem.Top.Bl.TrueLocal.nonempty_columnLocalData_of_standardConcreteFamily`.

*Proof.* The theorem on recursion gives the group compatibility with the recursion condition. The full Hermitian columns of the true columns give the tied Hermitian columns. These data and the two compatibilities give the column data at the split primes. $\square$

### The true volume stage

A stage $G$ over the columns of $w$ is good if for each later stage built on $G$ the volumes are tied, the gates have the right number, and the column data at the split primes exist. The volumes are tied if for each Hermitian space $W$ of admissible signature, each Haar measure $\mu$ of the right normalisation and each fundamental domain $\mathcal{F}$ of the rational points, $\mu(\mathcal{F}) = \mathrm{vol}(W)$ (see [Haar measure](/learn/analysis/#haar-measure)).

**Theorem 1.14.7 (A true volume stage).** Let $p$ be any property of column data. There is a column step from $p$ to the existence of a good stage over the columns of $w$.

Lean: `GlobalTheory.Mem.Top.Bl.TrueLocal.exists_trueVolume_stage_of_any_column_choice` (also `GlobalTheory.Mem.Top.Bl.TrueLocal.exists_trueVolumeStage_columnChoiceStep`, the case where $p$ is "pinned").

*Proof.* Step 1. Since the context is over the base, $w$ has a later stage $Z_0$. Step 2. The [standard column comparisons](/entry/cols-tied-sym-std/) give tied symmetric columns $C$ at $Z_0$ that are standard and standard in level. Step 3. The proposition on local families gives a local family $g$ for $C$. Step 4. Let $G$ be the stage of $Z_0$ with the true volumes, the true global datum and the gates $g$. The number of gates follows from the recursion condition, so two conditions remain. Step 5. The true volume is the volume of the unitary adelic quotient, so the volumes are tied. Step 6. The corollary on column data gives the column data at the split primes. The compatibility with $\omega$ holds for the true datum: two twelfth roots $\delta$, $\delta'$ of the discriminant differ by a root of unity $u$ with $u^{12} = 1$, so the invariants $g_2$ and $g_3$ of their lattices change by $u^{-4}$ and $u^{-6}$, which are a cube root of unity and a sign, and these lie in the coefficient field. Step 7. The local family moves from $Z_0$ to each later stage built on $G$. $\square$

**Remark 1.14.8 (Formalization).** In [ExistsGIs.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGIs.lean#L146) the proof opens with `StepW.of_all fun K B f T w hO _ _` and drops the property $p$ and the forced primes, so the case "pinned" at line 162 does not use the pin. The lemma `isLocalFamily_stages` (line 79) is proved by a `run_tac` block that assigns the hypothesis to the goal with `m.assign`; the kernel still checks the term. The local identification is `LocId` ([CompletionIntegersIff.lean](lean:Formalism/LocalToGlobal/GroupLattices/LevelGatherings/CompletionIntegersIff.lean#L16)), and the existence theorem is at line 444 of [ExistsLocIdOfCompletions.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLocIdOfCompletions.lean#L444), with the orbit indexing at lines 256 and 286. The recursion condition `IsRecG` and the gate count are not unfolded here.
