---
title: Inert theta admissibility
decls:
  - GlobalTheory.TwV.Lt.inert_theta_admissibility_of_complex_multiplication
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Inert theta admissibility

Section 5 assumed the inert admissibility hypothesis: at an inert prime, the pending tuple of a formal group system is admitted once a list of local conditions holds. This section proves that hypothesis from a statement on lattices with complex multiplication: each such lattice has a good Weierstrass model at every prime $l \ge 5$ prime to its discriminant. The result is used by the service row of Section 6, as its hypothesis 5, and through it by [the service row from Artin reciprocity](/entry/serv-h-row-of-artin/).

### Good models of CM lattices

Let $L \subset \mathbb{C}$ be the lattice of a period pair, with lattice invariants $g_2(L)$ and $g_3(L)$; we do not unfold their definition here. Let $d \ge 1$ be a squarefree integer with $d \equiv 3 \pmod 4$, and put

$$
\omega_d = \frac{1 + i\sqrt{d}}{2}.
$$

Then $\omega_d$ is a root of $x^2 - x + (1 + d)/4$, and $\mathbb{Z}[\omega_d]$ is the ring of integers of $\mathbb{Q}(\sqrt{-d})$. We say that $L$ *has complex multiplication by* $d$ if $\omega_d L \subseteq L$. Since $L$ is a group, this means that $L$ is a module over $\mathbb{Z}[\omega_d]$.

Let $l$ be a prime, $\mathbb{C}_l$ the completion of an algebraic closure of $\mathbb{Q}_l$, and $\mathbb{Q}_l^{\mathrm{ur}} \subset \mathbb{C}_l$ the maximal unramified extension of $\mathbb{Q}_l$.

**Definition 5.13.1 (Good model).** Let $\iota : \mathbb{C} \to \mathbb{C}_l$ be a ring isomorphism. A pair $(g_2, g_3)$ of elements of $\mathbb{C}_l$ is a *good model* of $L$ at $(l, \iota)$ if:
1. $g_2, g_3 \in \mathbb{Q}_l^{\mathrm{ur}}$;
2. $|g_2| \le 1$ and $|g_3| \le 1$;
3. $|g_2^3 - 27 g_3^2| = 1$;
4. there is $\lambda \in \mathbb{C}_l$ with $\lambda \ne 0$, $g_2 = \lambda^4 \iota(g_2(L))$ and $g_3 = \lambda^6 \iota(g_3(L))$.

Condition 4 says that $(g_2, g_3)$ is a change of scale of the invariants of $L$, moved to $\mathbb{C}_l$ by $\iota$. A change of scale $\lambda$ multiplies $g_2^3 - 27 g_3^2$ by $\lambda^{12}$ and does not change the ratio $g_2^3 / (g_2^3 - 27 g_3^2)$. Conditions 1 to 3 say that the rescaled invariants are unramified, integral, and have a unit discriminant. So a good model gives a Weierstrass equation $y^2 = 4x^3 - g_2 x - g_3$ with unramified integral coefficients and a unit discriminant.

**Definition 5.13.2 (CM good model condition).** The *CM good model condition* says: for every squarefree $d$ with $d \equiv 3 \pmod 4$, every lattice $L$ with complex multiplication by $d$, every prime $l \ge 5$ with $l \nmid d$ and every ring isomorphism $\iota : \mathbb{C} \to \mathbb{C}_l$, the lattice $L$ has a good model at $(l, \iota)$.

The condition $l \nmid d$ says that $l$ is unramified in $\mathbb{Q}(\sqrt{-d})$, since the discriminant of this field is $-d$. The CM good model condition is proved from global Artin reciprocity in [the theorem on good models of CM lattices](/entry/cm-good-model-of-global-artin-reciprocity/). Here we take it as a hypothesis.

### The inert admissibility hypothesis

We restate the hypothesis of Section 5 with all its data. Let $D$ be a datum with size data $L$, gate ties, an instance, a lattice instance, constants and primes $Q_p$. Let $\mathrm{ex}$ be extra data over $D$ and $t$ a tied kernel entry for $\mathrm{ex}$. Let $u$ be a word, $\mu$ a tuple and $w$ a place with its index condition, whose residue characteristic $p$ is prime. Take a filling of the gate of $(u, w)$, levels, a chain, and the kernel of the twist at $\mu$ for this chain. Take the local data of a formal group system at the gate, an embedding of its coefficient field, finiteness of the classes and of the stabilizers, a formal group with a Lubin-Tate isomorphism, and a bijection between the positions of the places of the system and the set of positions of $D$. Take a twist, comparison inputs $I$, level $0$ data, an element $a \in \mathcal{O}_E$ and a finite bad set of places of $F$. Finally take a curve ideal $\mathfrak{c}$, a complex number $\delta$, a base $B$, a character $\chi$, a ring map $\lambda : \overline{\mathbb{Q}} \to \mathbb{C}_p$, a finite set of places of $E$, a number $c_l$, a family $\Xi_0$ of functions between the level classes, and a family $\mu_T$ of functions on the finite ideles of $E$. These data build a pending tuple $P$ of the system.

**Definition 5.13.3 (Inert admissibility hypothesis).** The *inert admissibility hypothesis* says: for all data as above, if
1. the curve condition holds for $(\mathfrak{c}, \delta, B, \chi, \lambda)$ and the formal group at $p$,
2. the hypotheses on the theta series data below the top level hold,
3. the local factorization law holds,
4. the stabilizer law holds, and
5. there are ties of $P$ with $t$ at every level $j < m$, read through the kernel of the twist at $\mu$,

then the pending tuple $P$ is admitted.

**Theorem 5.13.4 (Inert theta admissibility).** Assume the CM good model condition. Then the inert admissibility hypothesis holds.

Lean: `GlobalTheory.TwV.Lt.inert_theta_admissibility_of_complex_multiplication`

*Proof.* This is [the theorem on admissible entries of small chains](/entry/admissible-entries-small-chain/), which proves the inert admissibility hypothesis under the CM good model condition. $\square$

**Remark 5.13.5 (Formalization).** Several facts about the Lean code:
1. The CM good model condition is `Formalism.L2.Th1.CM.CM2` and a good model is `IsGoodModel` (Formalism/LocalToGlobal/TorsionIntegrality/CMGoodModels/Statement.lean:45 and :38). Complex multiplication by $d$ is `HasCMBy d L`, the inclusion $\omega_d L \subseteq L$ (line 10), with $\omega_d$ = `omegaK d` (line 8).
2. The theorem `admissible_entries_small_chain` is stated under `variable [Fact CM2] in` (Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/AdmissibleEntriesOfKernelLaw.lean:105). So the proof first makes the hypothesis an instance with `haveI : Fact CM2 := ⟨h⟩` (InertThetaAdmissibilityOfComplexMultiplication.lean:9).
3. `AdmAtEnt2` has two definitions with the same text: `GlobalTheory.TwV.Lt.AdmAtEnt2` (Development/AbelianVarietyTheory/Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean:106) and `Formalism.L2.KerInert.AdmLoc2.AdmAtEnt2` (Formalism/LocalToGlobal/InertKernelTheory/ThetaSeriesDataHypothesesBelowMaximalLevel.lean:98). The theorem states the first and proves it with a term of the second, so the two agree by unfolding.
4. The pending tuple `pendG`, the conditions `CurveIn`, `ThetaSeriesDataHypothesesBelowMaximalLevel`, `XiIn`, `LawInLt`, `TiesAt` and `admitted`, and the lattice invariants `L.g₂` and `L.g₃`, are not unfolded here. Section 5 reads `XiIn` as the local factorization law and `LawInLt` as the stabilizer law.
