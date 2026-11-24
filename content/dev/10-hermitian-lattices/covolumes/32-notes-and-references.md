---
title: Notes and references
decls:
  - GlobalTheory.FlagBase.SiegelStep.glVol_step
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Notes and references

The chapter feeds three steps of the proof. The step [nonempty hypotheses](/step/nonempty-hyps/) uses most of it: the weights of terms near the reference lattice, the type bound, the covolumes of the integral unipotent radical and of the stabilizers of relevant terms, the mass of a genus of local data and its product form, the local nongeneric bound with its kernel of moves, the masses of self-dual Hermitian lattices, the generic mass bound and the archimedean facts about discrete series. The step [every character of the literature](/step/every-character-of-literature/) uses the modulus of the Levi subgroup of an isotropic flag on its unipotent radical. The step [every character](/step/every-character/) uses the [Siegel step for lattice volumes](/entry/gl-vol-step/) and the orbit contribution of a single pair to the mean over line lattices. Two of the results are conditional: the row positivity of Section 29 assumes a Siegel-Weil formula for unitary groups in its convergent range, and the lowest K-type statement of Section 28 is derived from a compression formula that is taken as a hypothesis. Neither assumption is proved in the chapter.

### Weights, orbit sums and frame classes (Sections 1 to 5)

The weight of a term is a ratio of covolumes of arithmetic subgroups of one unipotent group, and the bounds of the first five sections are bookkeeping for such ratios: an index of one lattice stabilizer in another is a ratio of covolumes, and a sum over orbits weighted by inverse stabilizer sizes is a mass. The normal form of a pair of isotropic flags is the linear algebra of the Bruhat decomposition of a unitary group relative to a parabolic subgroup. The comparison of sums over row lattices with sums over a genus of definite lattices in Section 5 is a form of the gluing of lattices along a common sublattice, as in the classical computation of masses of lattices from masses of their orthogonal pieces; the precise statements, the [datum bounds](/entry/sum-weights-per-datum/) and the [pair count](/entry/pair-count-bound-of-siegel-mass/) are specific to the double coset sum of the proof and have no classical source that we know of.

### The amplitude at a real place (Sections 6, 7, 8 and 25)

The fibre volumes and the amplitude bounds at a real place are integrals over a unipotent subgroup of $U(r + k, r + 1)$, computed in coordinates given by leading minors. The method is the elementary one: write the integrand in the coordinates of the flag, cut the domain into dyadic ranges of a Gram volume, and bound the volume of each range. The covolume of the reference lattice stabilizer is the volume of a nilmanifold. The theory of lattices in nilpotent Lie groups, which shows that such a covolume is finite and can be computed in exponential coordinates, is due to Malcev; see Raghunathan, *Discrete Subgroups of Lie Groups*, Chapter II. The general position case of Section 25 is the case where the integral converges absolutely and its size is governed by the Gram number; the bound is our computation.

### The type bound and the global terms (Sections 9 to 12)

The amplitude of a term factors as the covolume of an integral stabilizer times local factors, as an adelic orbital integral factors into local orbital integrals. The [type bound](/entry/type-bound-of-gap/) combines the amplitude bound with a count of pairs. The rational witnesses of Section 11 rest on the fact that a rational point of a unipotent group which is integral at every finite place lies in the integral group; this is elementary for unipotent groups because the exponential map is defined over the rationals. The formula of Section 12 for the double coset sum over one row is an unfolding of the sum along the orbits of the rational group.

### Strong approximation, row lattices and the mass identity (Sections 13 to 15)

Strong approximation for a unipotent group over a number field holds with respect to any nonempty set of places, since the group is isomorphic as a variety to an affine space and the rationals are dense in the finite adeles for the additive group. For semisimple simply connected groups the statement is due to Kneser and Platonov; see Platonov and Rapinchuk, *Algebraic Groups and Number Theory*, Chapter 7, and Kneser (1966). The chapter uses only the unipotent case. The [mass identity](/entry/weights-add-up-to-mass/) of Section 15 is the analogue, for the terms of the double coset sum, of the group-theoretic form of the mass formula of Smith, Minkowski and Siegel: a sum over the classes in a genus of the inverse orders of the stabilizers equals the volume of an adelic quotient. Siegel (1935) proved the formula for quadratic forms with an explicit product of local densities. The finiteness of the number of classes in a genus and the finiteness of covolumes for arithmetic subgroups are theorems of Borel and Harish-Chandra (1962).

### The covolume of the integral unipotent radical (Sections 16 and 23)

The [covolume of the integral unipotent radical](/entry/covolume-n/) is computed exactly. The computation is the unipotent case of the volume of an arithmetic quotient, where all local factors are trivial and the answer is a power of the discriminant times a normalization of the Haar measure. For semisimple groups the analogous exact formula is the volume formula of Prasad (1989), which writes the covolume of a principal arithmetic subgroup as a product of the discriminant, the Euler factors and the local volumes of parahoric subgroups; Borel and Prasad (1989) used it to prove finiteness theorems for discrete subgroups of bounded covolume. The bound of Section 23 for the covolume of the stabilizer of a relevant term by a power of the height of its Gram matrix is a reduction statement for the integral points of a unipotent group fixing two flags; it is our computation.

### Bessel maps and formal degrees (Sections 17, 18 and 28)

The bound of the Hilbert-Schmidt norm of the archimedean amplitude by the inverse formal degree in Section 18 is a form of the Schur orthogonality relations for square-integrable representations: for a discrete series representation $\sigma$ with formal degree $d_\sigma$, the integral of $|\langle \sigma(g) u, v\rangle|^2$ over $G$ is $\|u\|^2 \|v\|^2 / d_\sigma$. The theory of the discrete series and of the formal degree is due to Harish-Chandra; the existence of the discrete series and the formula for the formal degree are in Harish-Chandra (1966). The infinitesimal character of a discrete series representation and its relation to the Harish-Chandra parameter are also from that work, and the Harish-Chandra isomorphism that identifies the center of the enveloping algebra with Weyl group invariants is in Knapp, *Lie Groups Beyond an Introduction*, Chapter V. The statement in Section 28 that the constant terms of square-integrable matrix coefficients vanish along a unipotent radical is a decay statement in the spirit of the Howe-Moore theorem on the vanishing of matrix coefficients at infinity (Howe and Moore, 1979); the proof in the chapter is a direct argument with a one-parameter torus. The use of the lowest K-type follows the theory of the discrete series, where the lowest K-type determines the representation; in the chapter this is reached through a compression formula assumed as a hypothesis.

### Moves, kernels and the local nongeneric bound (Sections 19 and 20)

The [local amplitude bound](/entry/amp-le-mass/) is proved with an invariant symmetric kernel on the terms whose rows sum to almost $1$ and whose rows twisted by the phase sum to almost $0$. This is a version of the averaging arguments used to bound exponential sums over orbits of $p$-adic groups. The construction of the kernel by moves and the [saving for terms with a nonzero defect](/entry/amp-sq-nonzero-defect/) are specific to the proof.

### Masses of self-dual lattices and primitive tuples (Sections 21, 22 and 24)

The [mass bounds](/entry/mass-bounds/) for self-dual Hermitian lattices with a fixed intersection with a subspace rest on the comparison of Section 22 between the content of a set of primitive tuples and the content of the set of their Gram matrices. This is the local density statement behind the Siegel mass formula: the density of representations of a Hermitian matrix by a Hermitian lattice is a limit of normalized counts of solutions modulo powers of a prime, and for a primitive representation the counts stabilize. The chapter needs only a crude form, up to a factor $2$, and no exact value of the local densities. For unitary groups, the exact mass formula with explicit local factors is due to Gan, Hanke and Yu (2001), following Shimura. The count of frame classes over a sublattice in Section 24 is a counting argument with heights and has no classical source that we know of.

### Haar measure, generic masses and thin tubes (Sections 26 and 27)

The integration formula of Section 26 over the big cell is the Bruhat form of the Haar measure of a reductive group: on the open Bruhat cell $\bar N M A N$ the Haar measure is a product of Haar measures of the factors with a density given by the modular function; see Knapp, *Lie Groups Beyond an Introduction*, Chapter VIII. The chapter computes the constant exactly for the measure normalized by the Hilbert-Schmidt metric. The small fundamental sets of Section 27 are a reduction statement for the real points of a unipotent group modulo its integral points, in the spirit of reduction theory; see Borel and Harish-Chandra (1962) and Platonov and Rapinchuk, Chapter 4. The asymptotic volume of thin tubes in a product of unitary groups is an elementary consequence of the local Euclidean structure of the Haar measure near the identity. The generic mass bound of Section 27 uses the mass law of Section 29 as a hypothesis.

### Genus masses and Siegel-Weil (Section 29)

The product form of the mass of a genus of local data is the Siegel mass formula in its adelic form: the mass of a genus is the covolume of an adelic stabilizer, and changing the stabilizer at finitely many places multiplies the mass by the corresponding local index ratios. See Siegel (1935) for quadratic forms, Weil (1965) for the adelic formulation and the Siegel-Weil formula for classical groups, and Gan, Hanke and Yu (2001) for unitary groups. The row positivity is derived from the Siegel-Weil formula for unitary groups in its convergent range. The regularized Siegel-Weil formula beyond that range is due to Kudla and Rallis (1994) for symplectic and orthogonal pairs and to Ichino (2004) for unitary pairs. The chapter assumes the convergent statement and does not prove it.

### The modulus of an isotropic flag (Section 30)

The conjugation modulus of the Levi subgroup on the unipotent radical is the modular character $\delta_P(m) = |\det \operatorname{Ad}(m)|_{\mathfrak n}|$ of the parabolic subgroup $P = M N$; see Knapp, *Lie Groups Beyond an Introduction*, Chapter VIII. The layer product of Section 30 writes it in terms of the sizes of the Levi element on the layers of the flag, with the Haar measure normalized by the Hilbert-Schmidt metric at the identity.

### The Siegel step for lattice volumes (Section 31)

The induction on the rank $j$ for the volume of the space of $\mathcal{O}_E$-lattices over a totally complex field $E$ is the inductive step of Siegel's computation of the volume of the space of lattices, through his mean value theorem: the mean over unimodular lattices of the sum of a function over the nonzero lattice points equals the integral of the function (Siegel, 1945). The values $\zeta_E(j)$ that appear are the special values of the Dedekind zeta function that occur in the classical formula for the covolume of $SL_n(\mathcal{O}_E)$. The mirabolic class functions of the last part of Section 31 are the finite field analogue of the restriction to the mirabolic subgroup in the theory of derivatives of Bernstein and Zelevinsky (1977); for the representation theory of $GL_n$ over a finite field in this language see Zelevinsky (1981).

### References

- A. Borel and Harish-Chandra, *Arithmetic subgroups of algebraic groups*, Ann. of Math. 75 (1962), 485 to 535.
- A. Borel and G. Prasad, *Finiteness theorems for discrete subgroups of bounded covolume in semi-simple groups*, Publ. Math. IHÉS 69 (1989), 119 to 171.
- I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. École Norm. Sup. (4) 10 (1977), 441 to 472.
- W. T. Gan, J. P. Hanke and J.-K. Yu, *On an exact mass formula of Shimura*, Duke Math. J. 107 (2001), 103 to 133.
- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), 1 to 111.
- R. Howe and C. C. Moore, *Asymptotic properties of unitary representations*, J. Funct. Anal. 32 (1979), 72 to 96.
- A. Ichino, *A regularized Siegel-Weil formula for unitary groups*, Math. Z. 247 (2004), 241 to 277.
- M. Kneser, *Strong approximation*, in *Algebraic Groups and Discontinuous Subgroups*, Proc. Sympos. Pure Math. 9, Amer. Math. Soc., 1966, 187 to 196.
- A. W. Knapp, *Lie Groups Beyond an Introduction*, second edition, Progress in Mathematics 140, Birkhäuser, 2002, Chapter V and Chapter VIII.
- S. S. Kudla and S. Rallis, *A regularized Siegel-Weil formula: the first term identity*, Ann. of Math. 140 (1994), 1 to 80.
- V. Platonov and A. Rapinchuk, *Algebraic Groups and Number Theory*, Pure Appl. Math. 139, Academic Press, 1994, Chapter 4 (reduction theory) and Chapter 7 (strong approximation).
- G. Prasad, *Volumes of S-arithmetic quotients of semi-simple groups*, Publ. Math. IHÉS 69 (1989), 91 to 117.
- M. S. Raghunathan, *Discrete Subgroups of Lie Groups*, Ergebnisse der Mathematik 68, Springer, 1972, Chapter II.
- C. L. Siegel, *Über die analytische Theorie der quadratischen Formen*, Ann. of Math. 36 (1935), 527 to 606.
- C. L. Siegel, *A mean value theorem in geometry of numbers*, Ann. of Math. 46 (1945), 340 to 347.
- A. Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965), 1 to 87.
- A. V. Zelevinsky, *Representations of Finite Classical Groups: A Hopf Algebra Approach*, Lecture Notes in Math. 869, Springer, 1981.
